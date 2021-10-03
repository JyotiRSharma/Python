import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="password")

print('Connected to DB')

'''
db={}
if parser.has_section(section):
    params=parser.items(section)
    for param in params:
        db[param[0]] = param[1]

else:
    raise Exception('Section {0} not found in the {1 fie'.format(section, filename))

'''

#  cursor
cur = conn.cursor()

for i in range(100):
    cur.execute("INSERT INTO PERSON (id, first_name, last_name, gender, date_of_birth) VALUES (%s, %s, %s, %s, %s)",
                (8009*100+i, 'Markus'+str(i), 'Zukerberg', 'M','24-09-1998'))

cur.execute("SELECT id, first_name FROM PERSON WHERE first_name='Mark'")
#execute the query
#cur.execute("SELECT * FROM PERSON LIMIT 10")

rows = cur.fetchall()

for r in rows:
    print(f" Id = {r[0]} Name = {r[1]}")

cur.close()

conn.commit()
conn.rollback()
conn.close()
