import sqlite3
from ariadne import (
    QueryType,
    MutationType,
    make_executable_schema,
    load_schema_from_path,
)
from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route, Mount
from starlette.responses import HTMLResponse


# Function to serve the Playground HTML
def playground(request):
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>GraphQL Playground</title>
            <link href="https://cdn.jsdelivr.net/npm/graphql-playground-react@1.7.20/build/static/css/index.css" rel="stylesheet" />
            <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react@1.7.20/build/static/js/middleware.js"></script>
        </head>
        <body>
            <div id="root"></div>
            <script>
                window.addEventListener('load', function (event) {
                    GraphQLPlayground.init(document.getElementById('root'), { endpoint: '/graphql' })
                });
            </script>
        </body>
        </html>
    """
    )


# Load GraphQL schema from the file
type_defs = load_schema_from_path("schema.graphql")
query = QueryType()
mutation = MutationType()


# Database connection helper
def get_db_connection():
    connection = sqlite3.connect("books.db")
    connection.row_factory = sqlite3.Row
    return connection


# Query resolvers
@query.field("books")
def resolve_books(*_):
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return [dict(book) for book in books]


@query.field("book")
def resolve_book(_, info, id):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (id,)).fetchone()
    conn.close()
    return dict(book) if book else None


@query.field("authors")
def resolve_authors(*_):
    conn = get_db_connection()
    authors = conn.execute("SELECT * FROM authors").fetchall()
    conn.close()
    return [dict(author) for author in authors]


@query.field("author")
def resolve_author(_, info, id):
    conn = get_db_connection()
    author = conn.execute("SELECT * FROM authors WHERE id = ?", (id,)).fetchone()
    conn.close()
    return dict(author) if author else None


# Mutation resolvers
@mutation.field("createBook")
def resolve_create_book(_, info, authorId, title, releaseYear):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO books (title, releaseYear, authorId) VALUES (?, ?, ?)",
        (title, releaseYear, authorId),
    )
    new_book_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    new_book = conn.execute(
        "SELECT * FROM books WHERE id = ?", (new_book_id,)
    ).fetchone()
    conn.commit()
    conn.close()
    return dict(new_book)


@mutation.field("updateBook")
def resolve_update_book(_, info, id, authorId=None, title=None, releaseYear=None):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (id,)).fetchone()
    if book:
        conn.execute(
            "UPDATE books SET title = COALESCE(?, title), releaseYear = COALESCE(?, releaseYear), authorId = COALESCE(?, authorId) WHERE id = ?",
            (title, releaseYear, authorId, id),
        )
        conn.commit()
        updated_book = conn.execute(
            "SELECT * FROM books WHERE id = ?", (id,)
        ).fetchone()
        conn.close()
        return dict(updated_book)
    conn.close()
    return None


@mutation.field("deleteBook")
def resolve_delete_book(_, info, id):
    conn = get_db_connection()
    conn.execute("DELETE FROM books WHERE id = ?", (id,))
    if conn.changes() == 0:
        return {"message": "Book not found", "errorCode": 404}
    conn.commit()
    conn.close()
    return {"message": "Book deleted successfully"}


# Assemble the schema
schema = make_executable_schema(type_defs, query, mutation)

# Starlette application
app = Starlette(
    debug=True,
    routes=[
        Mount("/graphql", GraphQL(schema, debug=True)),
        Route("/playground", playground),
    ],
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
