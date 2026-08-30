#!/usr/bin/python3

"""Module that exports all employees' TODO lists to JSON."""

import json
import requests


if __name__ == "__main__":

    try:
        base_url = "https://jsonplaceholder.typicode.com"

        users_response = requests.get(
            "{}/users".format(base_url)
        )
        users_data = users_response.json()

        data = {}

        for user in users_data:
            user_id = user.get("id")
            username = user.get("username")

            todos_response = requests.get(
                "{}/todos?userId={}".format(base_url, user_id)
            )
            todos_data = todos_response.json()

            tasks = []

            for task in todos_data:
                tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

            data[str(user_id)] = tasks

        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(data, jsonfile)

    except Exception as e:
        print("An error occurred: {}".format(e))
