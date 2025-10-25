# Mini-Library-Management-System

# Mini Library Management System

## Files
- operations.py       : Core library functions
- demo.py             : Demonstration script
- tests.py            : Assert-based tests
- UML.png             : UML diagram (hand-drawn style)
- DesignRationale.pdf : Short design rationale (1 page)
- README.md           : This file

## How to run
1. Run demo:
   python demo.py

2. Run tests:
   python tests.py

## Notes
- Data is kept in-memory (no persistent database); restarting the script clears data.
- Genres are validated against a fixed tuple: ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Education")
- Borrow limit per member: 3 books.
- Deletion rules: cannot delete a book if copies are currently borrowed; cannot delete a member with borrowed books.