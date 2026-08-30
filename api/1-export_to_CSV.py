#!/usr/bin/python3

"""Module that exports employee TODO list to CSV."""

import csv
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

            filename = "{}.csv".format(employee_id)

            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

                for task in todos_data:
                    writer.writerow([
                        employee_id,
                        username,
                        task.get("completed"),
                        task.get("title")
                    ])

        except Exception as e:
            print("An error occurred: {}".format(e))
