# Student Grade Management System

## Overview

The Student Grade Management System is a Python-based program that allows users to manage student records, calculate scores, and generate batch-wise topper lists. This system is designed to store student information in a MySQL database and perform various operations such as adding, removing, updating, and displaying student records.

## Features

- **Add Student**: Add a new student record, including name, course, assessments, and assignments.

- **Remove Student**: Remove a student record by providing the student ID.

- **Update Student**: Update the information for a specific student by providing the student ID.

- **Show All Students**: Display all student records in the system.

- **Batch-wise Topper List**: Display the batch-wise topper list for each course.

## Requirements

- Python 3.x
- MySQL Database

## Setup

1. Install the required Python packages:

   ```bash
   pip install mysql-connector-python

2. Set up a MySQL database named pythonprojectsdb with the necessary table. You can use the following SQL query to create the table:

   ```bash
   CREATE TABLE tblStudent (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    stud_name VARCHAR(255),
    course VARCHAR(255),
    assessment INT,
    assignment INT
   );

3. Update the MySQL database connection details in the student.py file:

   ```bash
   mydb = mysql.connector.connect(host="localhost",user="root",password="",database="pythonprojectsdb")

## Usage

1. Run the main.py file to start the Student Grade Management System. Follow the on-screen instructions to perform various operations.
