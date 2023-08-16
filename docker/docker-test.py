import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='my-secret-pw',
    host='localhost',
    port='13306'
)

cursor = cnx.cursor()
cursor.execute('select * from sapu_db.users')

for id, name in cursor:
    print(f'{id}: {name}')