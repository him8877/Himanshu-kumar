import mysql.connector

try:
    # Connecting to MySQL Workbench
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Him@8850",
        database="Himanshu"
    )
    cursor = conn.cursor()

    # Create table Employee
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS yourdata ( id INT, name VARCHAR(255),age INT, dept VARCHAR(25))''')

    # Insert data into MySQL Employee
    cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (88, 'Himanshu', 25, 'MCA'))
    cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (68, 'Ankit', 30, 'MCA'))
    cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (89, 'Rohit', 22, 'Btech'))

    # Commit the transaction
    conn.commit()

    # Read data from Employee
    cursor.execute("SELECT * FROM yourdata")
    rows = cursor.fetchall()
    print("Read Operations:")
    for row in rows:
        print(row)

    # Update data in Employee
    cursor.execute("UPDATE yourdata SET age = %s WHERE name = %s AND dept = %s", (15, 'Himanshu', 'MCA'))
    conn.commit()
    print("Update operation successful.")

    #Delete data from Employee
    cursor.execute("DELETE FROM yourdata WHERE name = %s AND dept = %s", ('Rohit', 'MCA'))
    conn.commit()
    print("Delete operation successful.")
    
    # Read data again to verify changes
    cursor.execute("SELECT * FROM yourdata")
    rows = cursor.fetchall()
    print("Read Operations after Update and Delete:")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
