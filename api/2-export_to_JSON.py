#!/usr/bin/python3

"""Module that exports employee TODO list to JSON."""

import json
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
                "{}/users/{}".format(base_url, employee_id)
            )
            user_data = user_response.json()

            username = user_data.get("username")

            todos_response = requests.get(
                "{}/todos?userId={}".format(base_url, employee_id)
            )
            todos_data = todos_response.json()

            tasks = []

            for task in todos_data:
                tasks.append({
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                })

            data = {
                str(employee_id): tasks
            }

            filename = "{}.json".format(employee_id)

            with open(filename, "w") as jsonfile:
                json.dump(data, jsonfile)

        except Exception as e:
            print("An error occurred: {}".format(e))
