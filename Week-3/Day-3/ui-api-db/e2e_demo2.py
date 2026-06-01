import requests
import mysql.connector
# -----------------------
# DB Connection
# -----------------------
try : 
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="company_db"
    )
    cursor = conn.cursor()
    sql = "select * from employees where name = 'nishi'"
    # sql = "select * from employees"
    cursor.execute(sql)
    record = cursor.fetchone()
    emp_name =  record[1]
    print("Employee name from db : ",emp_name)
    assert emp_name == "nishi"
    print("UI Vs DB Emplyoyee name verified successfully")
finally : 
    cursor.close()
    conn.close()