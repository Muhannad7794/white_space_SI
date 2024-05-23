import sqlite3


def create_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            releaseYear INTEGER,
            authorId INTEGER,
            FOREIGN KEY(authorId) REFERENCES authors(id)
        )
    """
    )

    # Add some initial data
    cursor.execute("INSERT INTO authors (name) VALUES ('Author One')")
    author_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO books (title, releaseYear, authorId) VALUES ('Book One', 2020, ?)",
        (author_id,),
    )
    cursor.execute(
        "INSERT INTO books (title, releaseYear, authorId) VALUES ('Book Two', 2021, ?)",
        (author_id,),
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_db()
