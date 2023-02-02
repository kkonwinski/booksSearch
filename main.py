from app.books_adapter import FreeBooksAdapter
from app.chat_gbt import ChatGbtAdapter


class Application:
    def main(self):
        adapter = FreeBooksAdapter()
        author_name = input('Podaj imię autora: ')
        authors = adapter.get_authors(author_name)
        for author in authors:
            print(author)

        search_author_id = int(input('Podaj numer autora, którego chcesz zobaczyć: '))
        found_author = next(filter(lambda x: x.author_id == search_author_id, authors))
        author_books = adapter.get_author_books(found_author.slug, adapter.API_URL)
        books = adapter.get_books_details(author_books)
        for book in books:
            print(book)


if __name__ == '__main__':
    app = Application()
    app.main()
