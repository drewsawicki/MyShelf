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

The **Reading Progress Tracker** is controlled via command-line arguments. Below are the commands for each mode:

### General Syntax:
   ```bash
   python main.py <mode> [<arguments>]
   ```

The **Reading Progress Tracker** is controlled via command-line arguments. Below are the commands for each mode:


### Available Modes:
1. **Add a Book**
   - Adds a new book to your reading list.
   - **Required Arguments**:
     - `--title <book_title>`: The title of the book.
   - **Optional Arguments**:
     - `--author <book_author>`: Author of the book (for api accuracy).
   - Example:
     ```bash
     python main.py add --title "The Great Gatsby" --author "F. Scott Fitzgerald"
     ```

2. **Update Progress**
   - Updates the current page number of an existing book.
   - **Required Arguments**:
     - `--title <book_title>`: The title of the book to update.
     - `--page <current_page>`: The page number the user is currently on.
   - Example:
     ```bash
     python main.py update --title "The Great Gatsby" --page 75
     ```

3. **List Books**
   - Lists all books in your reading list.
   - **No Arguments** required.
   - Example:
     ```bash
     python main.py list
     ```

4. **Show Book Details**
   - Displays detailed information about a specific book.
   - **Required Arguments**:
     - `--title <book_title>`: The title of the book.
   - Example:
     ```bash
     python main.py details --title "The Great Gatsby"
     ```

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