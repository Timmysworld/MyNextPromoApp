from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import employee,admin
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/create')
def create():

    return render_template('employeeform.html')

# CREATE EMPLOYEE 
@app.route('/create/employee' ,methods=['POST'])
def create_employee():
    print(".....EMPLOYEE IS REGISTERING.....")
    account = admin.Admin.get_account_by_admin_id(session['admin_id'])['id']
    print(account)
    employee_data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "gs_level": request.form['gs_level'],
        "veteran": request.form['veteran'],
        "years_of_service": request.form['years_of_service'],
        "potential_hire": request.form['potential_hire'],
        "edu_level": request.form['edu_level'],
        "position_id": request.form['positions'],
        "account_id": account
    }

    # employee_data2 ={
    #     "positions":request.form['positions'],
    #     "collateral_duties": request.form['collateral_duties'],
    # }

    # employee_data_Array ={
    #     "certifications":  [],
    #     "other_qualification": [],
    # }

    
    employee_id = employee.Employee.create_employee(employee_data)
    print("I just got REGISTERED")
    # employee_data2["employee_id"] = employee_id
    # employee_info = employee.Employee.create_employee(employee_data2)
    # employee_data_Array[""]
    print("-------- employee_info ---------")
    return redirect ('/admin/dashboard')
