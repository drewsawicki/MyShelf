# Reading Progress Tracker

A command-line application for tracking reading progress across multiple books. This tool helps you keep track of the pages you've read, monitor your reading progress, and save updates to a JSON file for future reference.

## Features

- **Add New Books**: Add books by title, author, and total pages.
- **Update Reading Progress**: Log the pages you’ve read in a book.
- **Display Reading Stats**: View your progress for each book.
- **Save to JSON**: Automatically save book progress to a JSON file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/drewsawicki/MyShelf.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd MyShelf
    ```

3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Usage
The Reading Progress Tracker is controlled via command-line arguments. Use the following syntax to interact with the application:

   ```bash
   python main.py --mode <mode> --title <book_title> [--author <author>] [--pages <total_pages>] --page <current_page>
   ```

## Modes
* `add`: Add a new book.
* `update`: Update reading progress for an existing book.
* `list`: Display the list of books with progression stats.
* `details`: Display details of one book.

## Command-Line Arguments
* `--mode <add|update|list|details>`: Specify the operation to perform.
* `--title <book_title>`: Title of the book.
* `--author <author>`: (Optional) Author of the book.
* `--pages <total_pages>`: (Optional) Total number of pages in the book.
* `--page <current_page>`: Pages read for progress update.

## Contributing
Feel free to submit a pull request if you have suggestions, bug fixes, or additional features to add. All contributions are welcome!

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Add feature name"
   git push origin feature-name
   ```
4. Create a pull request on GitHub.