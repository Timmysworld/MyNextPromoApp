from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import admin, employee
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup')
def admin_signup():
    return render_template('signup.html')

@app.route('/signin')
def admin_sign():
    return render_template('signin.html')

# CREATE ADMIN --> DEF REGISTER_ADMIN
@app.route('/register/admin', methods=['POST'])
def register():
    print("going to register")
    is_admin_valid = admin.Admin.validate_admin(request.form)
    if not is_admin_valid:
        return redirect('/signup')
# entire registration validation 
    data2 = {
        "account_name": request.form['account_name'].title()
    }
    is_account_valid = admin.Admin.validate_admin_account(data2)
    if not is_account_valid:
        print("OMGOSHHHHHHHH")
        return redirect('/signup')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
# then creates admin user 
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
    }
# pulls admin email to register admin account 
    admin_id = admin.Admin.register_admin(data)
    print("I just got REGISTERED")
    print("CHECKING ACCOUNT NAME")
    # DICTIONARY TO INSERT ACCOUNT_NAME FOR ADMIN USERS #
    data2[ "admin_user_id"] = admin_id
    account = admin.Admin.register_admin_account(data2)
    print(account)
    session['admin_id'] = admin_id
    return redirect('/admin/dashboard')


@app.route('/login', methods=['POST'])
def login():
    print("YOU'RE ABOUT TO LOG IN")
    admin_in_database = admin.Admin.get_by_email(request.form['email'])
    print("CHECKING LOG INFO")
    if not admin_in_database:
        flash("Invalid Login Information", "login")
        return redirect('/signin')
    if not bcrypt.check_password_hash(admin_in_database.password, request.form['password']):
        flash("Invalid Login Information", "login")
        return redirect('/signin')
    session['admin_id'] = admin_in_database.id
    print("CLEAR FOR DATA")
    return redirect('/admin/dashboard')

@app.route('/admin/dashboard')
def admin_user_dashboard():
    if "admin_id" not in session:
        return redirect('/')
    logged_in_admin = admin.Admin.get_by_id(session["admin_id"])
    AllEmployees = employee.Employee.get_all_employees()
    AllPositions = employee.Employee.get_all_positions()
    return render_template('dashboard.html', logged_in_user = logged_in_admin,employees = AllEmployees, positions = AllPositions)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
