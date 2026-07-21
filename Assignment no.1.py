class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        self.books[book_id] = Book(book_id, title, author)
        print("Book added successfully!\n")

    def register_patron(self):
        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")

        self.patrons[patron_id] = Patron(patron_id, name)
        print("Patron registered successfully!\n")

    def borrow_book(self):
        patron_id = int(input("Enter Patron ID: "))
        book_id = int(input("Enter Book ID to borrow: "))

        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.available:
                book.available = False
                patron.borrowed_books.append(book.title)
                print("Book borrowed successfully!\n")
            else:
                print("Book is already borrowed.\n")
        else:
            print("Invalid Patron ID or Book ID.\n")

    def return_book(self):
        patron_id = int(input("Enter Patron ID: "))
        book_id = int(input("Enter Book ID to return: "))

        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.title in patron.borrowed_books:
                book.available = True
                patron.borrowed_books.remove(book.title)
                print("Book returned successfully!\n")
            else:
                print("This patron did not borrow this book.\n")
        else:
            print("Invalid Patron ID or Book ID.\n")

    def display_books(self):
        if not self.books:
            print("No books in library.\n")
            return

        print("\nLibrary Books")
        print("-" * 40)
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(f"ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {status}")
            print("-" * 40)


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.register_patron()
    elif choice == 3:
        library.borrow_book()
    elif choice == 4:
        library.return_book()
    elif choice == 5:
        library.display_books()
    elif choice == 6:
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice! Please try again.")