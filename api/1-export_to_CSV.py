#!/usr/bin/python3

"""
This script fetches an employee's TODO list from the JSONPlaceholder REST API
and exports all of their tasks into a CSV file.
"""

import sys
import requests
import csv


def get_employee_todo_progress(employee_id):
    """
    Fetches employee details and their associated tasks,
    then exports the tasks to a CSV file.
    """

    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch employee information
        user_url = f"{base_url}/users/{employee_id}"
        user_response = requests.get(user_url)

        # If employee is not found, handle gracefully
        if user_response.status_code != 200:
            print(f"Error: Employee with ID {employee_id} not found.")
            return

        # Convert employee information from JSON into a Python dictionary
        employee = user_response.json()

        # Get the employee's name
        employee_name = employee.get("name")

        # Get the employee's username
        employee_username = employee.get("username")

        # Fetch TODO list items belonging to the employee
        todos_url = f"{base_url}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)

        # Stop and report an error if the TODO request failed
        todos_response.raise_for_status()

        # Convert the TODO data from JSON into a Python list
        tasks = todos_response.json()

        # Create the CSV filename using the employee ID
        filename = f"{employee_id}.csv"

        # Open the CSV file for writing
        with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:

            # Create a CSV writer
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            # Write the required CSV header
            writer.writerow([
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ])

            # Write every task belonging to the employee
            for task in tasks:
                writer.writerow([
                    employee_id,
                    employee_username,
                    task.get("completed"),
                    task.get("title")
                ])

        print(f"Data successfully exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the REST API: {e}")


if __name__ == "__main__":

    # Ensure exactly one argument (the employee ID) is passed
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    # Validate that the provided parameter is an integer
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Error: The employee ID must be an integer.")
        sys.exit(1)

    # Run the function using the employee ID
    get_employee_todo_progress(emp_id)
