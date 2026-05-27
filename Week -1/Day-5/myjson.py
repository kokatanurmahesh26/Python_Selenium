#CSV
# import csv
#Example
# data = [
#     {'id','name','score'},
#     {'1','alice','85'},
#     {'2','','78'}]

#Example-2
# import json
# with open("user.json", "r") as file :
#     data = json.load(file)
#     for user in data:
#         if user["version"]> 5.1 :
#             print("Name : ", user["name"])
#             print("ID : ", user["id"])
#             print("Language :", user["language"])
#             print("Version : ", user["version"])

#Example 3 - log file read
import logging
with open("logdata.log", "r") as file :
     for line in file:
        if "DEBUG" in line :
            print("Failure Log found")
            print(line.strip())

