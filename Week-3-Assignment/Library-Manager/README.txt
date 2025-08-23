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

#Note: But for now, this application only have certain Features(with one actor librarian) for librarian only but it could extent a bit more for student as well so actor could be two for now.
This application just contains very basic feature at starting but it could contains many more as per bussiness requirement. for eg. 
If end user or bussiness wants a feature like please add a new books with different gerne into library then the main actor
would be the higher manager(whomever placing the request/proposal) and librarian would be child actor who will work on that basis.
Basically, a fine library management system can contains features like,
1. adding books, viewing books, deleting books, issuing books to sutdents, modify or edit the details of the books, 
can view stocks of the books, order books, replace or re-order books, prepare books condition reports to higher manager, 
list of books taken books available count, get student feedbacks, align with higher manager request to buy new books.
if that would be the feature then we can multiple actors like, librarian, student, higher management, finance, vendors/supplier etc.



## How to Run
1. Clone the repository 
  git clone https://github.com/DipakNeupane1/mse-assignment-dipak-neupane
  cd mse-assignment-dipak-neupane
  git checkout psd
  cd Week-3-Assignment/Library-Manager
  then enter the command :: python main_application.py