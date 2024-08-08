import sqlite3

connect = sqlite3.connect('eto.db')


# connect.execute('''CREATE TABLE CUSTOM(
#     ID  INT PRIMARY KEY NOT NULL,
#     NAME CHAR(255) NOT NULL,
#     AGE INT NOT NULL,
#     DEPARTMENT TEXT NOT NULL
# )''')


connect.execute("INSERT INTO CUSTOM(ID, NAME, AGE, DEPARTMENT) VALUES(1, 'Umukoro David', 12, 'Python')")
connect.execute("INSERT INTO CUSTOM(ID, NAME, AGE, DEPARTMENT) VALUES(2, 'Damilare Kemi', 10, 'PHP')")

all_data = connect.execute('''SELECT * FROM CUSTOM''')
for i in all_data:
    print(i)

connect.close()