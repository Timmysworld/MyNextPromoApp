from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import admin
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup')
def admin_signup():
    return render_template('signup.html')

# CREATE ADMIN --> DEF REGISTER_ADMIN
@app.route('/register/admin', methods=['POST'])
def register():
    print("going to register")
    is_admin_valid = admin.Admin.validate_admin(request.form)
    if not is_admin_valid:
        return redirect('/signup')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "email": request.form['email'],
        "password": pw_hash,
    }
    admin_id = admin.Admin.register_admin(data)
    print("I just got REGISTERED")
    print("CHECKING ACCOUNT NAME")
    # DICTIONARY TO INSERT ACCOUNT_NAME FOR ADMIN USERS #
    data2 = {
        "account_name": request.form['account_name'],
        "admin_user_id": admin_id
    }
    is_account_valid = admin.Admin.validate_admin_account(data2)
    if not is_account_valid:
        print("OMGOSHHHHHHHH")
        return redirect('/signup')
    account = admin.Admin.register_admin_account(data2)
    print(account)
    session['admin_id'] = admin_id
    return redirect('/admin/dashboard')


@app.route('/login', methods=['POST'])
def login():
    admin_in_database = admin.Admin.get_by_email(request.form['email'])
    if not admin_in_database:
        flash("Invalid Login Information", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(admin_in_database.password, request.form['password']):
        flash("Invalid Login Information", "login")
        return redirect('/')
    session['admin_id'] = admin_in_database.id
    return redirect('/')
    # NEED TO ADD A ROUTE ^^^


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
