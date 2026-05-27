import requests
import csv

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Open CSV file
with open("Week-3\\Day-2\\data_driven\\user.csv", newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    # Loop through CSV rows
    for row in reader:

        print("\nExecuting API for:", row["name"])

        # Payload from CSV
        payload = {
            "name": row["name"],
            "username": row["username"],
            "email": row["email"]
        }

        # Send POST request
        response = requests.post(url, payload)
        print("response : ", response)
        # Convert response into JSON
        data = response.json()

        print("data : ", data)


        # Print response
        print("Status Code:", response.status_code)
        print("Response:", data)

        # Validations
        assert response.status_code == 201
        assert data["name"] == row["name"]
        assert data["email"] == row["email"]

        print("Validation Passed")