import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "mynd_helpdesk"
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)

	
#------------------------------- Fetch all result -------------

query = ("SELECT * FROM user_table")
mycursor = mydb.cursor()
mycursor.execute(query)
allresult = mycursor.fetchall()
for a in allresult:
	print(a)

#------------------------------- Fetch single result -------------

query = ("SELECT * FROM user_table")
mycursor = mydb.cursor()
mycursor.execute(query)
oneresult = mycursor.fetchone()
print(oneresult)
