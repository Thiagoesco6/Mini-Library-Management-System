"""
PROG211 - Object-Oriented Programming 1
Mini Library Management System
Core Operations Module
"""

# Data Structures as per requirements
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography", "History")

# Initialize data structures with actual books
books = {
    "9780451524935": {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Fiction",
        "total_copies": 3
    },
    "9780061120084": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "total_copies": 2
    },
    "9780141439518": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Fiction",
        "total_copies": 4
    }
}

members = [
    {
        "member_id": "M001",
        "name": "Alice Johnson",
        "email": "alice.johnson@email.com",
        "borrowed_books": []
    },
    {
        "member_id": "M002",
        "name": "Bob Wilson",
        "email": "bob.wilson@email.com",
        "borrowed_books": []
    }
]


def add_book(isbn, title, author, genre, total_copies):
    """
    Add a new book to the library system.
    """
    try:
        # Input validation
        if not isbn or not title or not author:
            return "Error: ISBN, title, and author are required!"

        if isbn in books:
            return "Error: Book with this ISBN already exists!"

        if genre not in genres:
            return f"Error: Invalid genre. Must be one of: {genres}"

        if total_copies < 0:
            return "Error: Total copies cannot be negative!"

        # Add the book
        books[isbn] = {
            "title": title,
            "author": author,
            "genre": genre,
            "total_copies": int(total_copies)
        }
        return "Book added successfully!"

    except Exception as e:
        return f"Error adding book: {str(e)}"


def add_member(member_id, name, email):
    """
    Add a new member to the library system.
    """
    try:
        # Input validation
        if not member_id or not name or not email:
            return "Error: Member ID, name, and email are required!"

        # Check if member ID already exists
        for member in members:
            if str(member["member_id"]) == str(member_id):
                return "Error: Member ID already exists!"

        # Add the member
        new_member = {
            "member_id": member_id,
            "name": name,
            "email": email,
            "borrowed_books": []
        }
        members.append(new_member)
        return "Member added successfully!"

    except Exception as e:
        return f"Error adding member: {str(e)}"


def search_books(search_term):
    """
    Search books by title or author.
    """
    try:
        if not search_term:
            return "Error: Search term is required!"

        results = []
        search_term_lower = search_term.lower()

        for isbn, book in books.items():
            if (search_term_lower in book["title"].lower() or
                    search_term_lower in book["author"].lower()):
                results.append({
                    "isbn": isbn,
                    "title": book["title"],
                    "author": book["author"],
                    "genre": book["genre"],
                    "total_copies": book["total_copies"]
                })

        if not results:
            return "No books found matching your search."

        # Format results for nice display
        formatted_results = f"Found {len(results)} book(s):\n"
        for book in results:
            formatted_results += f"- '{book['title']}' by {book['author']} (ISBN: {book['isbn']})\n"

        return formatted_results

    except Exception as e:
        return f"Error searching books: {str(e)}"


def borrow_book(member_id, isbn):
    """
    Borrow a book for a member.
    """
    try:
        # Find member
        member = None
        for m in members:
            if str(m["member_id"]) == str(member_id):
                member = m
                break

        if not member:
            return "Error: Member not found!"

        # Check book exists
        if isbn not in books:
            return "Error: Book not found!"

        book = books[isbn]

        # Check if member already has this book
        if isbn in member["borrowed_books"]:
            return "Error: Member already has this book borrowed!"

        # Check member hasn't reached borrowing limit (3 books)
        if len(member["borrowed_books"]) >= 3:
            return "Error: Member has reached borrowing limit (3 books)!"

        # Check if copies are available
        if book["total_copies"] <= 0:
            return "Error: No copies available for borrowing!"

        # Process borrowing
        member["borrowed_books"].append(isbn)
        book["total_copies"] -= 1

        return f"Book '{book['title']}' borrowed successfully by {member['name']}."

    except Exception as e:
        return f"Error borrowing book: {str(e)}"


def return_book(member_id, isbn):
    """
    Return a borrowed book.
    """
    try:
        # Find member
        member = None
        for m in members:
            if str(m["member_id"]) == str(member_id):
                member = m
                break

        if not member:
            return "Error: Member not found!"

        # Check if member has this book borrowed
        if isbn not in member["borrowed_books"]:
            return "Error: Member hasn't borrowed this book!"

        # Check book exists
        if isbn not in books:
            return "Error: Book not found in system!"

        # Process return
        book_title = books[isbn]["title"]
        member["borrowed_books"].remove(isbn)
        books[isbn]["total_copies"] += 1

        return f"Book '{book_title}' returned successfully by {member['name']}."

    except Exception as e:
        return f"Error returning book: {str(e)}"


def delete_book(isbn):
    """
    Delete a book from the system.
    """
    try:
        if isbn not in books:
            return "Error: Book not found!"

        # Check if any member has borrowed this book
        for member in members:
            if isbn in member["borrowed_books"]:
                return "Error: Cannot delete book - it is currently borrowed!"

        book_title = books[isbn]["title"]
        del books[isbn]
        return f"Book '{book_title}' deleted."

    except Exception as e:
        return f"Error deleting book: {str(e)}"


def display_all_books():
    """Display all books in the system."""
    if not books:
        print("No books in the system.")
        return

    print("\n=== ALL BOOKS ===")
    for isbn, book in books.items():
        print(f"ISBN: {isbn}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print(f"Available Copies: {book['total_copies']}")
        print("-" * 40)


def display_all_members():
    """Display all members in the system."""
    if not members:
        print("No members in the system.")
        return

    print("\n=== ALL MEMBERS ===")
    for member in members:
        print(f"Member ID: {member['member_id']}")
        print(f"Name: {member['name']}")
        print(f"Email: {member['email']}")
        print(f"Borrowed Books: {len(member['borrowed_books'])}")
        if member['borrowed_books']:
            for isbn in member['borrowed_books']:
                if isbn in books:
                    print(f"  - {books[isbn]['title']}")
        print("-" * 40)


# Additional utility functions
def get_book_count():
    return len(books)


def get_member_count():
    return len(members)


def get_available_books():
    available = []
    for isbn, book in books.items():
        if book['total_copies'] > 0:
            available.append(book['title'])
    return available