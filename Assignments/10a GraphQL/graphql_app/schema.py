# graphql_app/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Book


# Define a GraphQL type for the Book model
class BookType(DjangoObjectType):
    class Meta:
        model = Book


# Define a Query class with a resolver for fetching books
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()


# Define the schema with the Query class
schema = graphene.Schema(query=Query)
