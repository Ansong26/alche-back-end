#!/usr/bin/python3
"""Module that gathers data from an API for a given employee ID.

Fetches an employee's TODO list from the JSONPlaceholder REST API
and displays their task completion progress on the standard output.
"""
import requests

import sys


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Please provide a valid integer employee ID")
    else:
        try:
            base_url = "https://jsonplaceholder.typicode.com"

            user_response = requests.get(
                "{}/users/{}".format(base_url, employee_id))
            user_data = user_response.json()
            employee_name = user_data.get("name")

            todos_response = requests.get(
                "{}/todos?userId={}".format(base_url, employee_id))
            todos_data = todos_response.json()

            total_tasks = len(todos_data)
            completed_tasks = []
            for task in todos_data:
                if task.get("completed"):
                    completed_tasks.append(task)

            num_completed_tasks = len(completed_tasks)

            print("Employee {} is done with tasks({}/{}):".format(
                employee_name, num_completed_tasks, total_tasks))

            for task in completed_tasks:
                print("\t {}".format(task.get("title")))

        except Exception as e:
            print("An error occurred: {}".format(e))
