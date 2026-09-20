# Student Management System

## Description 
This is basic python project used to manage students records.It allows the user to add,view,search,update and delete Student Information

## Features
- Add Student
- View Student
- Search Student
- Update Student
- Delete Student
- Store student records in a text file
- Load student records from a file

## Technologies Used
- Python
- File Handling
- Exception Handling
- Input validation
- Exception handling

## Student Information

The system stores:

- Student Name
- Roll Number
- Marks

## Project Structure
Student_Management/
│
├── student_management.py
├── student.txt
├── README.md
└── .gitignore

## How to Run
1. Install Python.
2. Open the project folder.
3. Open the terminal in the project folder.
4. Run the Python program.

## Input Validation

The project validates the information entered by the user.

* Roll number must be a valid number.
* Marks must be between 0 and 100.
* Invalid input is handled using exception handling.
* Duplicate roll numbers are checked before adding a student.

## File Handling

The student records are stored in a text file named `student.txt`.

File handling is used to:

* Store student information permanently.
* Read student records when required.
* Update existing student information.
* Delete student information when required.

## Exception Handling

Exception handling is used to prevent the program from crashing when the user enters invalid data.

For example:

* `ValueError` is used to handle invalid numeric input.
* Other appropriate exceptions can be handled when required.

## Learning Outcomes

Through this project, I practiced:

* Variables and data types
* Lists
* Conditional statements
* Loops
* Functions
* User input
* File handling
* Exception handling
* Input validation

## Future Improvements

* Add a graphical user interface (GUI)
* Add more student details
* Improve the search functionality
* Add more file management features
* Improve the overall user interface
