from library_database import create_table
from library_manager import add_book, view_books, delete_book, issue_book_to_student, view_all_issued_books

def menu():
    print("\n==== Library Management System  ====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Delete Book by  Book ID")
    print("4. Issue Book to Student")
    print("5. View All Issued Books")
    print("6. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            author = input("Enter author: ")
            add_book(name, author)
        elif choice == '2':
            books = view_books()
            for book in books:
                print(book)
        elif choice == '3':
            book_id = int(input("Enter Book ID to Delete: "))
            delete_book(book_id)
        elif choice == '4':
            name = input("Enter name: ")
            address = input("Enter address: ")
            book_id = int(input("Enter Book ID: "))
            issue_book_to_student(name, address, book_id)
        elif choice == '5':
            issued_books = view_all_issued_books()
            for issued_book in issued_books:
                print(issued_book)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()