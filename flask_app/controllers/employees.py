from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import employee,admin,certification, collateral
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/create')
def create():
    if "admin_id" not in session:
        return redirect('/login')
    return render_template('employeeform.html', certifications=certification.Certifications.get_all_certifications(),  collateral = collateral.Collateral_Duties.get_all_collateral_duties()) # access the certification class function

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
        "account_id": account,
        
    }
    # sets employee id to the data from the form
    employee_id = employee.Employee.create_employee(employee_data)

    # list of all certifications an employee has then loops through and add the employee id to be inserted into the employee has certification table
    certs_list = request.form.getlist('certification')
    # print(certs_list)
    updated = ''
    for i in certs_list:
        # print(type(i))
        # updated += i[ : 3] + str(employee_id) + i[3 : ] + ','
        x = i.split(',')
        y =x[0]
        z = f"{y},{employee_id}),"
        print(z)
        updated += z
        # print(i)
    updated = updated[:-1]
    print(updated)

    certs_list = certification.Certifications.employee_cert_list(updated)

    # employee collateral duties #
    collateral_list = request.form.getlist('collateral_duties')
    # print(collateral_list)

    cd= ''
    for c in collateral_list:
        # print(c)
        # cd +=c[ : 3]  +  str(employee_id) + c[3 : ] + ','
        x = c.split(',')
        cid = x[0]
        z = f"{cid},{employee_id}),"
        print(z)
        cd += z
    cd = cd[:-1]
    # print(cd)

    collateral_list = collateral.Collateral_Duties.employee_cd_list(cd)

    print("I just got REGISTERED")
    print("-------- employee_info ---------")
    return redirect ('/admin/dashboard')

#READ EMPLOYEE: 
@app.route('/view/employee/<int:id>')
def view_employee(id):
    OneEmployee = employee.Employee.get_employee(id)
    # certs = certification.Certifications.get_all_certifications()
    cd = collateral.Collateral_Duties.get_all_collateral_duties()
    positions = employee.Employee.get_all_positions()
    # education = employee.Employee.get_all_edu_level(id)
    # certifications= certification.Certifications.get_certification_by_id(id)
    return render_template('show_employee.html', employee = OneEmployee, collateral=cd, position=positions)

#UPDATE EMPLOYEE:
@app.route("/edit/employee/<int:id>")
def edit_employee(id):
    if "admin_id" not in session:
        return redirect("/register")
    # data = {
    #     "id":id
    # }
    # user_data = {
    #     "id":session["user_id"]
    # }
    OneEmployee = employee.Employee.get_employee(id)
    positions = employee.Employee.get_all_positions()
    return render_template("edit_employee.html", employee = OneEmployee, position=positions)

# edit=employee.edit_one(data), user=admin.get_by_id(user_data)

@app.route("/update/employee/<int:id>", methods=["POST"])
def update_employee():
    if "user_id" not in session:
        return redirect("/register")
    if not employee.validate_employee(request.form):
        return redirect("/create/employee")
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "gs_level": request.form['gs_level'],
        "veteran": request.form['veteran'],
        "years_of_service": request.form['years_of_service'],
        "potential_hire": request.form['potential_hire'],
        "edu_level": request.form['edu_level'],
        "position_id": request.form['positions'],
    }
    employee.update(data)
    return redirect("/dashboard")

# DELETE EMPLOYEE
@app.route('/employees/delete/<int:id>')
def delete_employee(id):
    employee.Employee.delete_employee(id)
    return redirect('/admin/dashboard')
