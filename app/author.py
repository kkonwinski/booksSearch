class Author:
    def __init__(self, author_id: int, name: str, slug: str, api_books_url: str):
        self.author_id = author_id
        self.name = name
        self.slug = slug
        self.api_books_url = api_books_url

    def __str__(self):
        return f'{self.author_id}. {self.name}'
