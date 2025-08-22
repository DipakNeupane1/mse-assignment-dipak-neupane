# 📘 Library Management System (Command-Line Application)

## Project Overview
This is a command-line application developed as part of my classwork at **Yoobee Colleges**.  
The system manages library operations such as adding new books, deleting books, issuing books to students,
and generating a list of students who have borrowed books.

## Tech Stack
- **Programming Language**: Python
- **Database**: SQLite3
- **Tools**: Command-Line Interface (CLI)


## Features
- Adding new books to the library
- View added books
- Deleting books
- Issuing books to students
- Generating a list of students who have borrowed books from the library
- Persistent storage using SQLite3


#Week 4 - Activity 1: Design use case diagram
#Step 1: Write the number of actors and use cases for your college project,
defining the scope of the project in the same way as the activity completed in Week 3 for your college. 
#Share your GitHub Link with your scenario from Week 3.
 
## Use case
1. Actor is librarian --> add new books to the library.
2. Actor is librarian --> can view or list down the added books.
3. Actor is student  ---> can view or list down the available books.
4. Actor is librarian --> delete added books.
5. Actor is librarian --> issue books to sutdents.
6. Actor is librarian --> can view the list of students who has borrowed the books.
7. Actor is student --> can list the books what he/she have taken.

#Note: But for now, this application only have certain Features for librarian only but it could extent a bit more for student as well.


## How to Run
1. Clone the repository 
  git clone https://github.com/DipakNeupane1/mse-assignment-dipak-neupane
  cd mse-assignment-dipak-neupane
  git checkout psd
  cd Week-3-Assignment/Library-Manager
  then enter the command :: python main_application.py