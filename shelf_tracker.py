from datetime import datetime
import json
from utils import fetch_book_info

from datetime import datetime
from json import JSONDecodeError


# TODO: ADD TIMELINE FOR EACH BOOK

class Book:
    def __init__(self, title, author, total_pages, genre):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.genre = genre
        self.pages_read = 0
        self.start_date = str(datetime.now().date())
        self.updates = []  # Stores each progress update as {"date": date, "pages_read": pages}

    def update_progress(self, page):
        """Update the pages read for this book, if valid."""
        if page <= self.total_pages:
            self.updates.append({"date": str(datetime.now().date()), "pages_read": page - self.pages_read})
            self.pages_read = page
            print(f"Updated '{self.title}' progress to {page} pages.")
        else:
            print(f"Error: Total pages read cannot exceed {self.total_pages}.")

    def get_progress(self):
        """Calculate and return the progress percentage for this book."""
        progress = int((self.pages_read / self.total_pages) * 100)
        return f"{self.title} - {self.author}: {self.pages_read}/{self.total_pages} pages ({progress}%)."

    def to_dict(self):
        """Convert the book object to a dictionary format for easy JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "total_pages": self.total_pages,
            "pages_read": self.pages_read,
            "start_date": self.start_date,
            "updates": self.updates
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Book instance from a dictionary (used when loading from JSON)."""
        book = cls(data["title"], data["author"], data["total_pages"], data["genre"])
        book.pages_read = data["pages_read"]
        book.start_date = data["start_date"]
        book.updates = data["updates"]
        return book


class ShelfTracker:
    def __init__(self, filename='data/books.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """Load books objects from JSON file."""
        try:
            with open(self.filename, 'r') as f:
                book_data = json.load(f)
                return {title: Book.from_dict(attributes) for title, attributes in book_data.items()}
        except (FileNotFoundError, JSONDecodeError):
            return {}

    def save_books(self):
        """Convert books to dictionary objects and save to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump({title: book.to_dict() for title, book in self.books.items()}, f)
        except FileNotFoundError:
            return []

    def add_book(self, title, author=None):
        """Add book to shelf."""
        if title in self.books:
            print(f"{title} is already in your bookshelf.")
        else:
            book_info = fetch_book_info(title, author)
            if book_info:
                new_book = Book(
                    title=book_info["title"],
                    author=book_info["author"],
                    total_pages=book_info["total_pages"],
                    genre=book_info["genre"]
                )

                self.books[title] = new_book
                print(f"Added '{title}' by {book_info['author']} to your shelf.")
                self.save_books()
            else:
                print("Failed to retrieve book information.")

    def update_book_progress(self, title, page):
        """Update pages read for a book."""
        if title in self.books:
            self.books[title].update_progress(page)
            self.save_books()
            print(f"Updated progress for book: {title}")
        else:
            print(f"{title} is not in your bookshelf.")

    def list_books(self):
        """Print out all books in your shelf."""
        if self.books:
            for book in self.books.values():
                print(book.get_progress())
        else:
            print("No books yet.")

    def get_book_timeline(self, title):
        """Get the progress updates timeline for a specific book."""
        if title in self.books:
            updates = self.books[title].updates
            for update in updates:
                print(f"\t{update['date']}: {update['pages_read']} pages read.")
        else:
            print(f"{title} is not in your bookshelf.")

    def display_book_details(self, title):
        if title in self.books:
            book = self.books[title]
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Total Pages: {book.total_pages}")
            print(f"Pages Read: {book.pages_read}")
            print(f"Start Date: {book.start_date}")
            print(f"Genre: {book.genre}")
            print("Timeline:")
            self.get_book_timeline(title)
        else:
            print(f"{title} is not in your bookshelf.")


# TODO: IMPLEMENT DELETE FEATURE FOR BOOKS
# TODO: IMPLEMENT RECOMMENDATION FEATURE
# TODO: CREATE GUI

