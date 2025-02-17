import database
# calling the method from database.py
conn = database.get_db()
sql_query = "select * from todo"


#cursor : it is a pointer to table records as list of tuples
cursor  = conn.cursor()
cursor.execute(sql_query)
row = cursor.fetchall()
print(row)