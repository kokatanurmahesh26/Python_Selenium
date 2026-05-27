#dictionary
Contact = {"Name":"Mahesh", "Mob":"7654321"}

# #by using dict menthod
# Contact1 = dict(id = 100, name = "xyz")
# print(Contact1)

student = {"name": "rahul",
            "age" : "20",
            "mailid": "rahul123@gmail.com",
            "sub" : "CSE"}
print(student)

#Read dictionary
print(student["name"])

#update
student["age"] = 25
print(student)

#delete 
# del student["age"] 
# print(student)

print(student.keys()) #gives the keys details only
print(student.items()) #gives keys and values

print(student.get("name"))

#Update 
student.update({"name": "Mahesh"})
print(student)

#Pop
print(student.pop("name")) #Reomve the value
print(student)

#Nested Dictionary
test_data = {101 : {"status":"200", "msg":"success"}, 
             102 : {"status":"500", "msg":"internal server error"}}
print(test_data[101]["status"])
print(test_data[102]["msg"])


