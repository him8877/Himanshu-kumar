import mysql.connector

class Database:
    connection = None

    @classmethod
    def get_connection(cls):
        if cls.connection is None:
            cls.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Him@8850",
                database="Himanshu"
            )
        return cls.connection

class EmployeeModel:
    def __init__(self, id, name, age, dept):
        self.id = id
        self.name = name
        self.age = age
        self.dept = dept

    @staticmethod
    def create_table_if_not_exists():
        # Connect to MySQL
        db = Database.get_connection()
        cursor = db.cursor()
        # Create the yourdata table if it does not exist
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS yourdata (id INT ,name VARCHAR(255) NOT NULL,age INT,dept VARCHAR(255))"""
        cursor.execute(create_table_sql)
        db.commit()

    def save(self):
        # Connect to MySQL
        db = Database.get_connection()
        cursor = db.cursor()
        # Insert data into the yourdata table
        sql = "INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)"
        val = (self.id, self.name, self.age, self.dept)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def get_all():
        # Connect to MySQL
        db = Database.get_connection()
        cursor = db.cursor()
        # Retrieve all employees from the yourdata table
        cursor.execute("SELECT * FROM yourdata")
        rows = cursor.fetchall()
        employees = []
        for row in rows:
            employee = EmployeeModel(*row)
            employees.append(employee)
        return employees

    @staticmethod
    def get_by_id(id):
        # Connect to MySQL
        db = Database.get_connection()
        cursor = db.cursor()
        # Retrieve an employee by ID from the yourdata table
        cursor.execute("SELECT * FROM yourdata WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row:
            return EmployeeModel(*row)
        else:
            return None

    @staticmethod
    def update(id, name, age, dept):
        # Connect to MySQL
        db = Database.get_connection()
        cursor = db.cursor()
        # Update an employee in the yourdata table
        update_sql = "UPDATE yourdata SET name = %s, age = %s, dept = %s WHERE id = %s"
        val = (name, age, dept, id)
        cursor.execute(update_sql, val)
        db.commit()

    @staticmethod
    def delete(id):
        # Connect to MySQL
        db = Database.get_connection()
        cursor = db.cursor()
        # Delete an employee from the yourdata table
        delete_sql = "DELETE FROM yourdata WHERE id = %s"
        cursor.execute(delete_sql, (id,))
        db.commit()

    def __repr__(self):
        return f"{self.name}:{self.id}"
