#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")


Form=cgi.FieldStorage()
fName=Form.getvalue("Name")
fAddress=Form.getvalue("Address")
fNumber=Form.getvalue("Number")
fEmail=Form.getvalue("Email")

print("<h4>",fName,fAddress,fNumber,fEmail,"</h4>")
print("<h1>Thank you for your Order :)")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="table booking"
)

mycursor=mydb.cursor()

sql="INSERT INTO userfood(Name,Address,Number,Email)VALUES(%s,%s,%s,%s)";
value=(fName,fAddress,fNumber,fEmail)

mycursor.execute(sql,value)
mydb.commit()

print("</body>")
print("</html>")