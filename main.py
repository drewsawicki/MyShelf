import argparse
from datetime import datetime
from shelf_tracker import Book, ShelfTracker

# Initialize the reading tracker
tracker = ShelfTracker()

parser = argparse.ArgumentParser(description="Virtual Bookshelf Tracker")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Subparser for adding a book
add_book_parser = subparsers.add_parser("add", help="Add a new book to the tracker")
add_book_parser.add_argument("--title", required=True, help="Title of the book")
add_book_parser.add_argument("--author", required=True, help="Author of the book")
add_book_parser.add_argument("--pages", required=True, help="Total number of pages")

# Subparser for updating progress
update_progress_parser = subparsers.add_parser("update", help="Update progress on a book")
update_progress_parser.add_argument("--title", required=True, help="Title of the book")
update_progress_parser.add_argument("--page", required=True, help="Current page number")

# Subparser for listing books
list_parser = subparsers.add_parser("list", help="List all books and their progress")

# Subparser for displaying book details
book_details_parser = subparsers.add_parser("details", help="Get details about a book")
book_details_parser.add_argument("--title", required=True, help="Title of the book")

args = parser.parse_args()
if args.command == "add":
    if args.title and args.author and args.pages:
        tracker.add_book(args.title, args.author, int(args.pages))
    else:
        print("Please provide title, author, and total number of pages for the book.")
elif args.command == "update":
    if args.title and args.page:
        tracker.update_book_progress(args.title, int(args.page))
    else:
        print("Please provide title and current page number for the book.")
elif args.command == "list":
    tracker.list_books()
elif args.command == "details":
    if args.title:
        tracker.display_book_details(args.title)
    else:
        print("Please provide title of the book.")
else:
    parser.print_help()