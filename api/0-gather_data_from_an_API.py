#!/usr/bin/env python3
"""
This script fetches and displays the progress of an employee's TODO list
using the JSONPlaceholder REST API.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetches employee details and their associated tasks,
    then prints the progress to standard output in the exact format required.
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

        employee_name = user_response.json().get("name")

        # Fetch todo list items filtered by the given user/employee ID
        todos_url = f"{base_url}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        
        tasks = todos_response.json()
        
        # Compute tracking metrics
        total_tasks = len(tasks)
        completed_tasks = [task for task in tasks if task.get("completed") is True]
        number_of_done_tasks = len(completed_tasks)

        # Output the exact first line format required
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        
        # Output the titles of completed tasks with 1 tab and 1 space indentation
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

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

    get_employee_todo_progress(emp_id)

