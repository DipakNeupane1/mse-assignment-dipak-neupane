from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, add_student, view_students

#Week 3 - Activity 5: update the sample code "Sample_code_SQLite3"
#Please add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address.
# Insert two sample records into Students, then display all rows from both the Users and Students tables.

def menu():
    print("\n==== User and Student Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Add Students")
    print("6. View All Students")
    print("7. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-7): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        if choice == '5':
            name = input("Enter name: ")
            address = input("Enter address: ")
            add_student(name, address)
        elif choice == '6':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
