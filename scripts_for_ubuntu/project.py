import mysql.connector as ms
import time

SERVER_NAME = ('mysql')
DATABASE = 'project_kub'



cnx = ms.connect(user='root',passwd='1234', host=SERVER_NAME, database=DATABASE)
print("have connection to DB")
cur = cnx.cursor(buffered=True)
# the bufferd means that if you have read with fetchone not all information , you can run additional action with cur.execute()

# FOR TESTING - REMOVE LATER
cur.execute('drop table table1;')
cur.execute('CREATE TABLE `table1` ( `serial_n` int NOT NULL AUTO_INCREMENT,  `time_stamp` time DEFAULT NULL, PRIMARY KEY (`serial_n`) );')
#---------------------------------------
for i in range(1,11):
    cur.execute('INSERT INTO table1 (time_stamp) VALUE (CURRENT_TIME() ) ;')
    cnx.commit()
    print('row number [{}] inserted '.format(i))
    time.sleep(1)

cur.execute(' SELECT  serial_n,TIME_FORMAT(time_stamp, "%H:%i:%s") FROM table1;')
data = cur.fetchall()
print(data)
cnx.close()
