import pymysql

try:
    conn = pymysql.connect(host="localhost", user="root", password="P2615")
    print("Connection successful!")
except pymysql.MySQLError as e:
    print(f"Error: {e}")
