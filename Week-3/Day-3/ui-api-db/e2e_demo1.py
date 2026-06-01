import requests
import mysql.connector

# -----------------------
# UI Input
# -----------------------
name = input("Enter Employee Name: ")
position = input("Enter Job position: ")
salary = float(input("Enetr the salary:"))

# -----------------------
# API Call
# -----------------------
url = "https://reqres.in/api/users"

payload = {
    "name": name,
    "position": position,
    "salary" : salary
}

response = requests.post(url, json=payload)

print("API Status Code:", response.status_code)

# -----------------------
# DB Connection
# -----------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd",
    database="company_db"
)

cursor = conn.cursor()

# Insert data into DB
sql = """
INSERT INTO employees(name, position, salary)
VALUES (%s, %s, %f)
"""

# employee_id = 102

cursor.execute(sql, (name, position, salary))

conn.commit()

print("Data inserted into MySQL")

# -----------------------
# Validation
# -----------------------
cursor.execute(
    "SELECT * FROM employees where name = %s",(name,)
)


record = cursor.fetchone()

print("DB Record:", record)

cursor.close()
conn.close()