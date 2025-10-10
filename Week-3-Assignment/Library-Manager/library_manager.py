import sqlite3

from library_database import create_connection

# Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
# Use the sample code to develop a command-line application for Week 3 – Activity 4,
# incorporating a database sqlite3 and have at least three functionality such as add records,delete records
# and view records for different tables.
# Share the completed project on GitHub here, with including a README.txt file
# in your repository to describe the technical aspects of this project (Yoobee Colleges).


def add_book(name, author):
    conn = create_connection()
    conn.execute(
        "PRAGMA foreign_keys = ON;"
    )  # Enforce FK constraints while persisting data into db table.
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO books (name, author) VALUES (?, ?)", (name, author))
        conn.commit()
        print(" Book added successfully.")
    except sqlite3.IntegrityError:
        print("This book is already added.")
    conn.close()


def view_books():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_book(book_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("🗑️ Book deleted.")


def issue_book_to_student(name, address, book_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO student_books (name, address, book_id) VALUES (?, ?, ?)",
            (name, address, book_id),
        )
        conn.commit()
        print("Book is successfully issued to student.")
    except sqlite3.IntegrityError:
        print("This book is not available.")
    conn.close()


def view_all_issued_books():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_books")
    rows = cursor.fetchall()
    conn.close()
    return rows
