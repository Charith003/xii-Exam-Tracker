# xii-Exam-Tracker
XII Exam Tracker is a Python + MySQL CLI-based application for managing and tracking Class XII examination data efficiently. It allows you to store, update, search, and analyze student marks while maintaining a clean and persistent database structure for your school or practice needs.

Project Overview:
XII Exam Tracker is a Python + MySQL CLI-based application designed to manage and track Class XII examination data efficiently. It enables you to record, update, search, and analyze student marks while maintaining organized, persistent data storage for school administration or personal practice.
This project helps students and developers understand:
    Python-MySQL CRUD operations
    Menu-driven CLI app design
    Database connectivity in Python
    Basic data analysis like rank generation and filtering
    
Features:
   Add new marklists: Insert student marks, calculate total and percentage automatically
   Retrieve student marks: Search using Roll No and Exam Code
   Rank list generation: Display sorted rank list for a specific exam
   Update marks: Modify marks safely with auto recalculation
   Filter by percentage: Display students within a specific percentage range
   Manage absentees: Record and view absent students by subject and exam

Tech Stack:
   Python 3.x
   MySQL (via mysql-connector-python)
   CLI-based interface for easy navigation and lightweight operation.

Database Structure:

Database: exam_management
Table: exams
Column	Type	Description
rollno	INT	Student Roll Number
name	VARCHAR(100)	Student Name
exam	INT	Exam code (1, 2, 3)
engm	INT	English Marks
compm	INT	Computer Marks
phym	INT	Physics Marks
chemm	INT	Chemistry Marks
mathsm	INT	Maths Marks
total	INT	Total marks (auto calculated)
percent	FLOAT	Percentage (auto calculated)

Table: absentees
Column	Type	Description
rollno	INT	Student Roll Number
exam	INT	Exam Code
subject	INT	Subject Code (1-5)

