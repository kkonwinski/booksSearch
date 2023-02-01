# Overview
Python that uses the mysterious API from [Wolne Lektury Api](https://wolnelektury.pl/api/ "Wolne Lektury Api"). It's like a secret society of book lovers, and you're about to become a part of it.

We start off with a class called ****Author****, which is the blueprint for all the famous authors in the world. These authors have a unique ****author_id****, a name that's known to everyone, a slug that lets you identify them like a detective, and an ****api_books_url**** that will take you on a journey to discover all their books.

Next, we have the ****FreeBooksAdapter**** class that uses the get function from the requests library to communicate with the book enthusiasts at [Wolne Lektury Api](https://wolnelektury.pl/api/ "Wolne Lektury Api"). It retrieves information about all the authors and their books and is ready to be extended to uncover more secrets.

Finally, the ****Application**** class is where the real excitement takes place. It asks the user for the name of an author and then searches for all the authors with that name. It then prompts the user to select one of the authors by their unique ****author_id****, and displays all the books written by that author.

This project is the perfect blend of mystery, adventure, and entertainment. Get ready to embark on a journey to discover the world of books like never before!
# Class Descriptions
## Author: 
**This class represents an author and stores the following information:**

- *author_id*: a unique identifier for the author
- *name*: the name of the author
- *slug*: a string identifier for the author
- *api_books_url*: a URL to retrieve the author's books from the API

## FreeBooksAdapter: 
**This class uses the requests library to retrieve information from the Wolne Lektury API. It provides two methods:**

- **get_authors(search: str = None)**: retrieves a list of Author objects matching the search query. If no search query is provided, it returns all authors.
- **get_books(author_slug: str)**: retrieves a list of books for a given author slug.

## Application: 
This class provides a basic interface to interact with the book catalog. It prompts the user to input an author name, then displays a list of authors matching the name and allows the user to select one. Finally, it displays a list of books for the selected author.

# Usage
To run the code, simply execute the following in the command line:

Copy code
python main.py
where main.py is the name of the code file.