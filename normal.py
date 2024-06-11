import mysql.connector

# Connecting to MySQL Workbench
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Him@8850",
    database="Himanshu"
)

cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS yourdata (id INT, name VARCHAR(255), age INT, dept VARCHAR(255))
''')

# Insert data MySQL
cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (88, 'Himanshu', 25, 'MCA'))
cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (68, 'Ankit', 30, 'MCA'))
cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (89, 'Rohit', 22, 'Btech'))

# Commit 
conn.commit()

# Read data
cursor.execute("SELECT * FROM yourdata")
rows = cursor.fetchall()
print("Read Operations:")
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE yourdata SET age = %s WHERE name = %s AND dept = %s", (26, 'Ankit', 'MCA'))
conn.commit()

# Delete data 
cursor.execute("DELETE FROM yourdata WHERE name = %s AND dept = %s", ('Ankit', 'MCA'))
conn.commit()

# Close the MySQL connection
conn.close()
