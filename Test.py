# tests.py
from Operation import *


def run_tests():
    print("=== RUNNING LIBRARY SYSTEM TESTS ===\n")

    # Test 1: Add a valid book
    print("Test 1: Adding valid book...")
    result = add_book("978002", "Data Science", "Timothy Kamara", "Fiction", 3)
    assert result == "Book added successfully!", f"Failed: {result}"
    print("PASS")

    # Test 2: Add a member
    print("Test 2: Adding valid member...")
    result = add_member("2", "John Smith", "john@email.com")
    assert result == "Member added successfully!", f"Failed: {result}"
    print("PASS")

    # Test 3: Borrow a book
    print("Test 3: Borrowing book...")
    result = borrow_book("2", "978002")
    assert "borrowed successfully" in result, f"Failed: {result}"
    print("PASS")

    # Test 4: Return a book
    print("Test 4: Returning book...")
    result = return_book("2", "978002")
    assert "returned successfully" in result, f"Failed: {result}"
    print("PASS")

    # Test 5: Delete a book
    print("Test 5: Deleting book...")
    result = delete_book("978002")
    assert "deleted" in result, f"Failed: {result}"
    print("PASS")

    print("\n ALL TESTS PASSED SUCCESSFULLY!")


# Run the tests
run_tests()