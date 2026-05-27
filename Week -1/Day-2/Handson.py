users = [
    ["admin", "admin123"],
    ["qa", "qa123"],
    ["automation_user", "auto12345"],
    ["ab", "123"],
    ["tester01", "test@123"]
]

print("***Bulk User Validation***")

for user in users:
    username = user[0]
    password = user[1]

    print("\nchecking user : ", username)
    if len(username) >= 5 :
        if len(password) >=6 :
            print("Valid User")
        else : 
            print("Invalid id password")
    else : 
        print("Invalid Username")


#Hands2
#problem statement - An automation framework executes regression suites
#Rules - 
#Execute all test cases
#Skip disabled cases
#Stop execution if CRITICAL failure happens


#Automation Test Execution
test_cases = [
    ["Login Test", "ENABLED"],
    ["Payment", "ENABLED"],
    ["Camera Validation","DISABLED"],
    ["GPU Stress Test","ENABLED"],
    ["Critical ECU Test","Failed"],
    ["Bluetooth Test","ENABLED"]
]

for test in test_cases :
    test_name = test[0]
    status = test[1]

    #Skip disabled test cases
    if status == "DISABLED" :
        print("\nskipping : ", test_name)
        continue
    
    #Strop Execution on critical failure
    if status == "FAILED" :
        print("\nCritical failure found")
        print("Stopping execution : ", test_name)
        break
    print("\nExecutiing : ", test_name)
    print("Execution Successful")