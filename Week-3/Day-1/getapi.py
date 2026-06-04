import requests

# API URL
url = "https://dummyjson.com/users"

# Send GET request
response = requests.get(url)

# Print Status Code
print("Status Code:", response.status_code)

# Convert response into JSON
data = response.json()

# print("data text : ",response.text)

# Print total products
print("Total users:", data["total"])

# Print first product details
first_product = data["users"][2]

print("\nFirst Product Details")
print("----------------------")
print("Title:", first_product["firstName"])
print("Price:", first_product["lastName"])
print("Category:", first_product["age"])

# Validation
if response.status_code == 200:
    print("\nAPI Test Passed")
else:
    print("\nAPI Test Failed")