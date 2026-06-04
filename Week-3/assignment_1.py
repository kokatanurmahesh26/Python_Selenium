import requests
try : 
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    data = response.json()
    print(data)
    print("Name : ", data["name"])
     # Validation
    assert data["name"] == "Leanne Graham"
    print("Validated json data")

    if response.status_code == 200:
        print("API Test Passed")
    else:
        print("API Test Failed")
finally : 
    print("Execution completed for assignment 1")
