import requests

def fetch_book_info(title, author=None):
    query = f"intitle:{title}"
    if author:
        query += f"+inauthor:{author}"

    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            # Use the first search result
            book_info = data["items"][0]["volumeInfo"]
            # Extract details
            title = book_info.get("title", "Unknown Title")
            authors = book_info.get("authors", ["Unknown Author"])
            total_pages = book_info.get("pageCount", "N/A")
            genre = book_info.get("categories", ["Unknown Genre"])

            return {
                "title": title,
                "author": authors[0],  # Use the first author
                "total_pages": total_pages,
                "genre": genre[0]  # Use the first genre
            }
        else:
            print("No results found for this title.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None