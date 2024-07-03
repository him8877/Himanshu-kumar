from flask import Flask, render_template, request, redirect, abort
from model import EmployeeModel

app = Flask(__name__)

# Create the table if it does not exist
EmployeeModel.create_table_if_not_exists()

@app.route('/')
def index():
    return redirect('/data')

# Other routes for CRUD operations
@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        dept = request.form['dept']
        new_employee = EmployeeModel(id, name, age, dept)
        new_employee.save()
        return redirect('/data')

@app.route('/data')
def retrieve_list():
    employees = EmployeeModel.get_all()
    return render_template('datalist.html', employees=employees)

@app.route('/data/<int:id>')
def retrieve_employee(id):
    employee = EmployeeModel.get_by_id(id)
    if employee:
        return render_template('data.html', employee=employee)
    return f"Employee with id = {id} doesn't exist"

@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update_employee(id):
    employee = EmployeeModel.get_by_id(id)
    if request.method == 'POST':
        if employee:
            name = request.form['name']
            age = request.form['age']
            dept = request.form['dept']
            EmployeeModel.update(id, name, age, dept)
            return redirect(f'/data/{id}')
        abort(404)  # Should handle the case where employee is None

    return render_template('update.html', employee=employee)

@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete_employee(id):
    employee = EmployeeModel.get_by_id(id)
    if request.method == 'POST':
        if employee:
            EmployeeModel.delete(id)
            return redirect('/data')
        abort(404)  

    return render_template('delete.html', employee=employee)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

