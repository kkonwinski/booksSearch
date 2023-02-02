from requests import get


class Book:
    def __init__(self, slug: str, title: str, epoch: str, genre: str, book_id: int):
        self.book_id = book_id
        self.slug = slug
        self.title = title
        self.epoch = epoch
        self.genre = genre

    def __str__(self):
        return f'{self.book_id}. Tytuł: {self.title} - Typ: {self.genre} - Epoka: {self.epoch}'
