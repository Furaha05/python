
import sqlite3
conn=sqlite3.connect('mitjo.db')
print("open database successfull")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(1,'Furaha',20,'Emobilis','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(2, 'Furaha',20,'Emobilis','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(3, 'Furaha',20,'Emobilis','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(4, 'Furaha',20,'Emobilis','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(5, 'Furaha',20,'Emobilis','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(6, 'Furaha',20,'Emobilis','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(7, 'Furaha',20,'Emobilis','Female')")

conn.commit()
print("records added successfully")
conn.close()