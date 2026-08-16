Employee TODO API Project
Description
This project uses Python and the JSONPlaceholder REST API to retrieve employee information and TODO tasks.
The project demonstrates how to:
Connect to a REST API using Python.
Retrieve employee information.
Retrieve employee TODO tasks.
Display an employee's task progress.
Identify completed and incomplete tasks.
Export employee tasks to CSV.
Export employee tasks to JSON.
Export tasks from all employees into one JSON file.
Project Features
1. Employee TODO Progress
The program accepts an employee ID and retrieves their information and tasks.
It displays:
Employee name
Number of completed tasks
Total number of tasks
Titles of completed tasks
Example:
python3 script.py 1
2. Individual Employee CSV Export
The project can export all tasks belonging to a specific employee into a CSV file.
The CSV contains:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
The generated file is named:
USER_ID.csv
For example:
1.csv
Both completed and incomplete tasks are included.
3. Individual Employee JSON Export
The project can also export all tasks belonging to one employee into JSON format.
The generated file is named:
USER_ID.json
For example:
1.json
The JSON structure is:
{
    "1": [
        {
            "task": "TASK_TITLE",
            "completed": false,
            "username": "USERNAME"
        }
    ]
}
4. All Employees JSON Export
The project retrieves tasks belonging to all employees and stores them in one JSON file.
The generated file is:
todo_all_employees.json
Its structure is:
{
    "1": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": false
        }
    ],
    "2": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": true
        }
    ]
}
Technologies Used
Python 3
Requests library
JSON
CSV
JSONPlaceholder REST API
Installation
Install Python 3 and the Requests library:
pip install requests
Running the Project
For an individual employee:
python3 script.py <employee_id>
For example:
python3 script.py 1
The all-employees export can be run without an employee ID:
python3 script.py
API
The project uses:
https://jsonplaceholder.typicode.com
The API provides the employee and TODO information used by the scripts.
Error Handling
The scripts handle:
Invalid employee IDs
Missing employees
API connection errors
Failed API requests
Invalid command-line input
Purpose
This project demonstrates practical Python programming concepts, including REST API communication, data processing, loops, dictionaries, lists, JSON handling, CSV generation, file creation, and command-line arguments.
