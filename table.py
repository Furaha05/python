import sqlite3
conn=sqlite3.connect('listless.db')
print("Open database successfully")
conn.execute("CREATE TABLE wanafunzi ("
             "ID INT PRIMARY  KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("Tables created successfully")
conn.close()