import requests

# API URL
url = "https://dummyjson.com/users/1"


response = requests.delete(url)

# Print Status Code
print("Status Code:", response.status_code)

# Print JSON Response
data = response.json()

print("\nProduct Created Successfully")
print("----------------------------")
print("Product ID:", data["id"])
print("FirstName:", data["firstName"])
print("Deleted:", data["isDeleted"])

# Validation
assert response.status_code == 200
assert data["id"] == 1
assert data["isDeleted"] == True