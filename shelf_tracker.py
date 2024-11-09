from datetime import datetime
import json

from datetime import datetime
from json import JSONDecodeError


class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.pages_read = 0
        self.start_date = str(datetime.now().date())
        self.updates = []  # Stores each progress update as {"date": date, "pages_read": pages}

    def update_progress(self, page):
        """Updates the pages read for this book, if valid."""
        if page <= self.total_pages:
            self.pages_read = page
            self.updates.append({"date": str(datetime.now().date()), "pages_read": page - self.pages_read})
            print(f"Updated '{self.title}' progress to {page} pages.")
        else:
            print(f"Error: Total pages read cannot exceed {self.total_pages}.")

    def get_progress(self):
        """Calculates and returns the progress percentage for this book."""
        progress = int((self.pages_read / self.total_pages) * 100)
        return f"{self.title} - {self.author}: {self.pages_read}/{self.total_pages} pages ({progress}%)."

    def to_dict(self):
        """Converts the book object to a dictionary format for easy JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "total_pages": self.total_pages,
            "pages_read": self.pages_read,
            "start_date": self.start_date,
            "updates": self.updates
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Book instance from a dictionary (used when loading from JSON)."""
        book = cls(data["title"], data["author"], data["total_pages"])
        book.pages_read = data["pages_read"]
        book.start_date = data["start_date"]
        book.updates = data["updates"]
        return book


class ShelfTracker:
    def __init__(self, filename='data/books.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                book_data = json.load(f)
                return {title: Book.from_dict(attributes) for title, attributes in book_data.items()}
        except (FileNotFoundError, JSONDecodeError):
            return {}

    def save_books(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump({title: book.to_dict() for title, book in self.books.items()}, f)
        except FileNotFoundError:
            return []

    def add_book(self, title, author, total_pages):
        if title in self.books:
            print(f"{title} is already in your bookshelf.")
        else:
            self.books[title] = Book(title, author, total_pages)
            print(f"Added '{title}' by {author} to your shelf.")
            self.save_books()

    def update_book_progress(self, title, page):
        if title in self.books:
            self.books[title].update_progress(page)
            self.save_books()
            print(f"Updated progress for book: {title}")
        else:
            print(f"{title} is not in your bookshelf.")

    def list_books(self):
        if self.books:
            for book in self.books.values():
                print(book.get_progress())
        else:
            print("No books yet.")


