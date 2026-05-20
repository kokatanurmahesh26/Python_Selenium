
# username = input("Enter username : ").strip().lower()
# print(username[0].upper() + username[1: len(username)])


while True:
    try:
        username = input("Enter username : ").strip().lower()
        password = input("Enter Password : ").strip()
        assert username == "admin"
        assert password == "Admin@123"
        print("Login Successful")
        break
    except AssertionError :
     print("Invalid username or password")