import mysql.connector as ms

SERVER_NAME = ('mysql')
DATABASE = 'project_kub'
cnx = ms.connect(user='root',passwd='1234', host='mysql', database=DATABASE)
print("have connection to DB")
cur = cnx.cursor(buffered=True)
# the bufferd means that if you have read with fetchone not all information , you can run additional action with cur.execute()

cur.execute(' SELECT * FROM table1;')
data = cur.fetchall()
print(data)
cnx.close()
