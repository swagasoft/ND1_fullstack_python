import psycopg2

connection = psycopg2.connect("dbname='postgres' user='postgres' host='127.0.0.1' password='password' port='5432'")
cursor =  connection.cursor()

cursor.execute(''' 
CREATE TABLE  test (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
)
''')

cursor.execute(''' INSERT INTO test (id, completed)  VALUES (1, true) ''')

connection.commit()
connection.close()
cursor.close()