import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost"
	user = "root"
	passwd = "mynd_helpdesk"
)

print(mydb)