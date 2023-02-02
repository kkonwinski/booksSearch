from requests import get
from app.author import Author
from app.book import Book
import json


class FreeBooksAdapter:
    API_URL = "https://wolnelektury.pl/api/"

    def get_authors(self, search: str = None):
        authors = []
        query = get(self.API_URL + 'authors/')
        for author_id, author in enumerate(query.json(), start=1):
            if search is not None and search in author['name']:
                authors.append(Author(
                    author_id=author_id,
                    name=author.get('name'),
                    slug=author.get('slug'),
                    api_books_url=author.get('href', '') + 'books'
                ))
        return authors

    def get_books_details(self, author_books:list):
        books_list = []
        for book_id, book in enumerate(author_books, start=1):
            books_list.append(Book(
                book_id=book_id,
                slug=book.get('slug'),
                title=book.get('title'),
                epoch=book.get('epoch'),
                genre=book.get('genre')
            ))
        return books_list

    def get_author_books(self, author_slug: str, api_url: str):
        return get(f'{api_url}authors/{author_slug}/books').json()
