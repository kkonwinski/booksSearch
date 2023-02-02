from app.books_adapter import FreeBooksAdapter
from app.book import Book


class Application:
    def main(self):
        adapter = FreeBooksAdapter()
        author_name = input('Podaj imię autora: ')
        authors = adapter.get_authors(author_name)
        for author in authors:
            print(author)

        search_author_id = int(input('Podaj numer autora, którego chcesz zobaczyć: '))
        found_author = next(filter(lambda x: x.author_id == search_author_id, authors))
        books = Book()
        for book in books.get_books(found_author.slug, adapter.API_URL):
            print(book.get('title'))


if __name__ == '__main__':
    app = Application()
    app.main()
