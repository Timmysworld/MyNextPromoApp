from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt       
bcrypt = Bcrypt(app) 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$')

class Admin:
    db = "MyNextPromoApp"
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.password =data['password']
        self.created_at =data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_admin_account(data2):
        is_valid = True
        account_name_in_database = Admin.get_account_by_name(data2["account_name"])
        if account_name_in_database is not False:
            print("whyyyyyyyyy")
            flash("Account Name is already in use!","register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_admin(admin):
        is_valid = True
        admin_in_database = Admin.get_by_email(admin["email"])
        if len(admin['email']) == 0 or not EMAIL_REGEX.match(admin['email']):
            flash("Invalid email address!", "register")
            is_valid = False
        if admin_in_database is not False:
            flash("Email is already in use!","register")
            is_valid =False
        if len(admin['password'])<8 or not PASSWORD_REGEX.match(admin['password']):
            flash(
                    """
                        Password must contain each of the following:
                        <ul>
                            <li>minimum 8 characters</li>
                            <li>1 Uppercase & 1 Lowercase</li>
                            <li>1 special character</li>
                            <li>1 number</li>
                        </ul>
                    ""","register"
                )
            is_valid = False
        if admin['confirmPass'] != admin['password']:
            flash("Password does not Match Try Again", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(admin):
        is_valid =True
        admin_in_database = Admin.get_by_email(admin["email"])
        # HOW DO I CHECK LOGIN VALIDATION FOR SPECIFIED ACCOUNT 
        if len(admin['email']) == 0 or not EMAIL_REGEX.match(admin['email']):
            flash("Invalid email address!", "login")
            is_valid = False
        if admin_in_database is False:
            flash("Sorry, You're not register!","login")
            is_valid = False
        if len(admin["password"]) < 8 or not bcrypt.check_password_hash (admin_in_database.password,admin["password"]):
            flash("Invalid information", "login")
            is_valid = False
        if admin['confirmPass'] != admin['password']:
            flash("Password does not Match Try Again", "login")
            is_valid = False
        if is_valid:
            return admin_in_database
        else:
            return is_valid
        
    @classmethod
    def register_admin(cls,data):
        query = """
        INSERT INTO admin_users (first_name,last_name,email,password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s, %(password)s);
        """
        results= connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def register_admin_account(cls, data):
        query = """
        INSERT INTO accounts (account_name, admin_user_id)
        VALUES (%(account_name)s, %(admin_user_id)s);"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_account_by_name(cls,account_name):
        print(account_name)
        data2 ={"account_name":account_name}
        query = "SELECT * FROM accounts WHERE account_name = %(account_name)s;"
        
        result = connectToMySQL(cls.db).query_db(query,data2)
        print("this is my result from get_account_by_name")
        # print(result[0])
        if len(result) ==0:
            return False
        else:
            return result[0]
    
    @classmethod
    def get_account_by_admin_id(cls,admin_user_id):
        print(admin_user_id)
        data2 ={"admin_user_id":admin_user_id}
        query = "SELECT * FROM accounts WHERE admin_user_id = %(admin_user_id)s;"
        
        result = connectToMySQL(cls.db).query_db(query,data2)
        print("this is my result from get_account_by_admin_id")
        # print(result[0])
        if len(result) ==0:
            # print("=====GOTCHA=====")
            return False
        else:
            # print("++++GET EM++++")
            return result[0]

    @classmethod
    def get_by_email(cls,email):
        print(email)
        data = {"email": email}
        print(data)
        query = "SELECT * FROM admin_users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result, "*"*20)
        if len(result) == 0:
            return False
        else:
            return cls(result[0])
    
    @classmethod
    def get_by_id(cls,admin_id):
        print(admin_id)
        data = {"id":admin_id}
        print(data)
        query = "SELECT * FROM admin_users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result,"*"*20)
        return cls(result[0])