#
with open("abc.txt", "r") as file :
    for line in file :
        username, password = line.strip().split(",")
        print("execution started")
        print("username : ", username)
        print("password : ", password)