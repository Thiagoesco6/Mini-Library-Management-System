# demo.py
from Operation import *

print("=== LIBRARY MANAGEMENT SYSTEM DEMO ===")
print("\n1. Adding a new book:")
print(add_book("978801", "Python Basics", "Sana", "Non-Fiction", 5))

print("\n2. Adding a new member:")
print(add_member("1", "Caroline Banqura", "caroline@email.com"))

print("\n3. Searching for books:")
print(search_books("Python"))

print("\n4. Borrowing a book:")
print(borrow_book("1", "978801"))

print("\n5. Returning a book:")
print(return_book("1", "978801"))

print("\n6. Displaying all books:")
display_all_books()

print("\n7. Displaying all members:")
display_all_members()

print("\n=== DEMO COMPLETED ===")