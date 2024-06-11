import sqlite3

# Connect to the database
conn = sqlite3.connect('Himanshu')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, dept TEXT)''')

# Insert data
cursor.execute('''INSERT INTO users (name, age, dept) VALUES (?, ?, ?)''', ('Himanshu', 25, 'MCA'))
cursor.execute('''INSERT INTO users (name, age, dept) VALUES (?, ?, ?)''', ('Ankit', 30, 'MCA'))
cursor.execute('''INSERT INTO users (name, age, dept) VALUES (?, ?, ?)''', ('Rohit', 22, 'Btech'))

# Commit the changes
conn.commit()

# Read data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Read Operations:")
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE users SET age=? WHERE name=? AND dept=?", (26, 'Ankit', 'MCA'))
conn.commit()
    
# Delete data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Delete Operations:")
for row in rows:
    print(row)
    
# Update data
cursor.execute("DELETE users SET dept=? WHERE name=? AND dept=?", (26, 'Ankit', 'MCA'))
conn.commit()

# Close the connection
conn.close()