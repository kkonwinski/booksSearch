import openai
import os
from dotenv import load_dotenv


class ChatGbtAdapter:
    load_dotenv()

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    def prepare_response(self, question: str):
        openai.api_key = self.OPENAI_API_KEY
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}",
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )

    def show_response(self, response: dict = None):
        print(response.get('choices')[0].get('text'))

    def show_book_questions(self, found_author, found_book):
        return {
            'author': f'Opowiedz biografie autora: {found_author.name}',
            'book': f'Napisz opracowanie "{found_book.title}"',
            'epoch': f'Opowiedz coś o epoce {found_book.epoch}'
        }
