from requests import get


class Author:
    def __init__(self, author_id: int, name: str, slug: str, api_books_url: str):
        self.author_id = author_id
        self.name = name
        self.slug = slug
        self.api_books_url = api_books_url

    def __str__(self):
        return f'{self.author_id}. {self.name}'


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

    def get_books(self, author_slug: str):
        return get(f'{self.API_URL}authors/{author_slug}/books').json()


class Application:
    def main(self):
        adapter = FreeBooksAdapter()
        author_name = input('Podaj imię autora: ')
        authors = adapter.get_authors(author_name)
        for author in authors:
            print(author)

        search_author_id = int(input('Podaj numer autora, którego chcesz zobaczyć: '))
        found_author = next(filter(lambda x: x.author_id == search_author_id, authors))

        for book in adapter.get_books(found_author.slug):
            print(book.get('title'))


if __name__ == '__main__':
    app = Application()
    app.main()