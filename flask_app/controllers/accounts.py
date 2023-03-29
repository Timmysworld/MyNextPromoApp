from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import admin, employee
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/admin/account/<int:account_id>')
def accounts(account_id):
    if "admin_id" == account_id:
        return

