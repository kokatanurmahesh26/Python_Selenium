import requests
import mysql.connector

#UI
sname = input("Enter student Name: ")
sbranch = input("Enter branch: ")

#API
url = "https://reqres.in/api/users"

payload = {
    "name": sname,
    "position": sbranch
}
response = requests.post(url, json=payload)

print("API Status Code:", response.status_code)

#DB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="student_db"
)
cursor = conn.cursor()
# Insert data into DB
sql = """
INSERT INTO students(sname, sbranch)
VALUES (%s, %s)
"""
cursor.execute(sql, (sname, sbranch))
conn.commit()
print("Data inserted into MySQL")

#Validations
cursor.execute(
     "SELECT * FROM students WHERE sname = %s",
    (sname,)
)
record = cursor.fetchone()

print("DB Record:", record)

cursor.close()
conn.close()