from requests import get


class Book:
    def get_books(self, author_slug: str, api_url: str):
        return get(f'{api_url}authors/{author_slug}/books').json()
