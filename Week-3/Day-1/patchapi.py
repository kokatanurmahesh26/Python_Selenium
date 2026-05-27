import requests

# API URL
url = "https://dummyjson.com/users/1"

# Request Payload
payload = {
    "firstName": "travel",
}

# Send POST request
get_response = requests.get(url)
get_data =  get_response.json()
print("FirstName Before update:", get_data["firstName"])

response = requests.patch(url, json=payload)

# Print Status Code
print("Status Code:", response.status_code)

# Print JSON Response
data = response.json()

print("\nProduct Created Successfully")
print("----------------------------")
print("Product ID:", data["id"])
print("FirstName:", data["firstName"])

# Validation
if response.status_code == 200:
    assert data["firstName"] == "travel"
    print("\nPATCH API Test Passed")
else:
    print("\PATCH API Test Failed")