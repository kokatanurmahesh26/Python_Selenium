import requests

# API URL
url = "https://dummyjson.com/users/1"

# Request Payload
payload = {
    "firstName": "travel",
    "lastName": "with",
    "maidenName": "maahi"
}

# Send POST request
response = requests.put(url, json=payload)

# Print Status Code
print("Status Code:", response.status_code)

# Print JSON Response
data = response.json()

print("\nProduct Created Successfully")
print("----------------------------")
print("Product ID:", data["id"])
print("FirstName:", data["firstName"])
print("LirstName:", data["lastName"])
print("Middlename:", data["maidenName"])

# Validation
if response.status_code == 200:
    assert data["firstName"] == "travel"
    print("\nPUT API Test Passed")
else:
    print("\nPUT API Test Failed")