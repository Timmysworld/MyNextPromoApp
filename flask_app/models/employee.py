from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt       
bcrypt = Bcrypt(app) 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$')

class Employee:
    db = "MyNextPromoApp"
    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        # self.password = data['password'],
        self.position = data['position'],
        self.gs_level = data['gs_level'],
        self.veteran = data['veteran'],
        self.years_of_service = data['years_of_service'],
        self.potential_hire = data['potential_hire']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user():
        pass

    @classmethod
    def create_employee(cls,data):
        query = """
        BEGIN;

        INSERT INTO employees (first_name,last_name,email,position,gs_level,veteran,years_of_service,potential_hire)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(gs_level)s,%(veteran)s,%(years_of_service)s,%(potential_hire)s);

        INSERT INTO positions (title)
        VALUES (LAST_INSERT_ID(),%(title)s);

        INSERT INTO education_levels (edu_level)
        VALUES (LAST_INSERT_ID(),%(edu_level)s);

        INSERT INTO certifications (employee_id,name)
        VALUES (LAST_INSERT_ID(),%(employee_id)s,%(name)s);
        
        INSERT INTO other qualifications (certification)
        VALUES (LAST_INSERT_ID()%(certification)s);

        INSERT INTO collateral duties (name)
        VALUES (LAST_INSERT_ID(),%(name)s);
        
        COMMIT;"""
        return connectToMySQL(cls.db).query_db(query, data)
        # QUESTION: how will i hard code the value of each certification into the database and still be able to insert an employee with a SQL statement? 2. Need help understanding the (last insert id). Does it hold onto the employees id or just keep incrementing no matter the employee?
        # QUESTION: Do i need to add position to the employee class if i have a position table that i will be needing to insert the employee position to? being that the employee table is connected to the position table?  
