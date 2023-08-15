class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            print("Book not found in the library.")

    def display_books(self):
        print("Books in the library:")
        for book_id, book in self.books.items():
            availability = "Available" if book.is_available else "Not Available"
            print(f"Book ID: {book_id}, Title: {book.title}, Author: {book.author}, Status: {availability}")

    def borrow_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_available:
                book.is_available = False
                print(f"You have borrowed '{book.title}'.")
            else:
                print("Book is not available for borrowing.")
        else:
            print("Book not found in the library.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_available:
                book.is_available = True
                print(f"You have returned '{book.title}'.")
            else:
                print("This book is already in the library.")
        else:
            print("Book not found in the library.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)
            print("Book added successfully.")

        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == "5":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
