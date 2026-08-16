#!/usr/bin/env python3

"""
This script fetches all employees and their TODO tasks from the
JSONPlaceholder REST API and exports the data into a JSON file.
"""

import requests
import json


def get_all_employees_todo():
    """
    Fetches all employees and all TODO tasks, organizes the tasks
    by employee ID, and exports the data to a JSON file.
    """

    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch all employees
        users_url = f"{base_url}/users"
        users_response = requests.get(users_url)
        users_response.raise_for_status()

        # Convert employee data from JSON into a Python list
        users = users_response.json()

        # Fetch all TODO tasks
        todos_url = f"{base_url}/todos"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()

        # Convert TODO data from JSON into a Python list
        tasks = todos_response.json()

        # Create a dictionary to store all employees and their tasks
        all_employees_tasks = {}

        # Create a dictionary to quickly find usernames using employee IDs
        usernames = {}

        # Store each employee's username using their ID
        for user in users:
            usernames[user.get("id")] = user.get("username")

        # Go through every task
        for task in tasks:
            employee_id = task.get("userId")

            # If this employee does not yet have a task list, create one
            if str(employee_id) not in all_employees_tasks:
                all_employees_tasks[str(employee_id)] = []

            # Create the required task structure
            task_data = {
                "username": usernames.get(employee_id),
                "task": task.get("title"),
                "completed": task.get("completed")
            }

            # Add the task to the employee's task list
            all_employees_tasks[str(employee_id)].append(task_data)

        # Create the required JSON filename
        filename = "todo_all_employees.json"

        # Open the JSON file for writing
        with open(filename, mode="w", encoding="utf-8") as json_file:

            # Write all employee task data to the JSON file
            json.dump(all_employees_tasks, json_file, indent=4)

        print(f"Data successfully exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the REST API: {e}")


if __name__ == "__main__":
    get_all_employees_todo()
