"""
Date: 18 January 2021
Author: Sanam Kandar
Modified by: [Your Name]
Project: Student Library Manager
"""

from datetime import datetime


class Library:
    def __init__(self, initial_books):
        self.available_books = initial_books

    def show_books(self):
        print(f"\n📚 Currently Available ({len(self.available_books)}):")
        for book in self.available_books:
            print(f"   - {book}")
        print()

    def issue_book(self, student_name, book_title):
        if book_title not in self.available_books:
            print(f"⚠️ '{book_title}' is currently not available or already issued.\n")
        else:
            issued_books.append({student_name: book_title})
            self.available_books.remove(book_title)
            print(f"✅ '{book_title}' has been issued to {student_name}. Please return it on time.\n")

    def accept_return(self, book_title):
        print(f"📥 '{book_title}' has been returned. Thank you!\n")
        self.available_books.append(book_title)

    def accept_donation(self, book_title):
        print(f"🎁 Thank you for donating '{book_title}'!\n")
        self.available_books.append(book_title)


class Student:
    def borrow(self):
        print("🔍 Book Borrowing Process:")
        return input("Enter the book title you want to borrow: ").strip()

    def return_book(self):
        print("📤 Book Return Process:")
        student_name = input("Enter your name: ").strip()
        book_title = input("Enter the book title you are returning: ").strip()
        if {student_name: book_title} in issued_books:
            issued_books.remove({student_name: book_title})
        return book_title

    def donate(self):
        print("📦 Book Donation Process:")
        return input("Enter the title of the book you'd like to donate: ").strip()


def main():
    library = Library([
        "Vistas", "Invention", "Rich & Poor", "Indian Economy",
        "Macroeconomics", "Microeconomics"
    ])
    user = Student()
    global issued_books
    issued_books = []

    print("\n📚 Welcome to the Central Library 📚")
    print(f"📅 {datetime.now().strftime('%d %B %Y')}")
    print("-" * 50)

    options = {
        1: "View available books",
        2: "Borrow a book",
        3: "Return a book",
        4: "Donate a book",
        5: "View issued books",
        6: "Exit"
    }

    while True:
        print("\nChoose an option:")
        for key, value in options.items():
            print(f"{key}. {value}")

        try:
            choice = int(input("Your choice: "))

            if choice == 1:
                library.show_books()
            elif choice == 2:
                name = input("Enter your name: ").strip()
                book = user.borrow()
                library.issue_book(name, book)
            elif choice == 3:
                returned_book = user.return_book()
                library.accept_return(returned_book)
            elif choice == 4:
                donated_book = user.donate()
                library.accept_donation(donated_book)
            elif choice == 5:
                if issued_books:
                    print("\n📋 Issued Book Records:")
                    for record in issued_books:
                        for person, book in record.items():
                            print(f"'{book}' is currently with {person}.")
                else:
                    print("\n📭 No books are currently issued.")
            elif choice == 6:
                print("\n👋 Thank you for using the library system. Goodbye!\n")
                break
            else:
                print("❌ Invalid option! Please select a valid number.")
        except Exception as err:
            print(f"⚠️ Error: {err} — Please enter a valid number.\n")


if __name__ == "__main__":
    main()
