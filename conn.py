import mysql.connector


conn = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='12345678',
  database='space',
)
cursor = conn.cursor()




cursor.close()
conn.close()
