import requests
import json
#define base url
url = "https://reqres.in/api/users/2"

#send the http GET request
response = requests.get(url)

#Print status code
print(f" Status code : {response.status_code}")
print("Response Body Json : ")
print(response.json()) #print data in json format

assert response.status_code == "200", f"Expected 200, but got {response.status_code}"
json_data = response.json()
assert json_data["data"]["id"] == 2, "Thes user id does not match"
print("Test Passed : User fetched successfully")

