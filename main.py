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
        search_book_id = int(input('Podaj numer książki, którą chcesz zobaczyć: '))
        found_book = next(filter(lambda x: x.book_id == search_book_id, books))
        print(f'Wybrałeś książkę: {found_book.title}')

        chat_adapter = ChatGbtAdapter()
        questions = chat_adapter.show_book_questions(found_author, found_book)
        for question_id, question in enumerate(questions.values(), start=1):
            print(f'{question_id}. {question}')
        found_book_question = int(input('Wybierz pytanie: '))
        question = list(questions.values())[found_book_question - 1]
        if found_book_question == 2:
            question = question + ' autora: ' + found_author.name

        # response = chat_adapter.prepare_response(question)
        # chat_adapter.show_response(response)


if __name__ == '__main__':
    app = Application()
    app.main()
