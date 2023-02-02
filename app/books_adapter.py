from requests import get
from app.author import Author


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


