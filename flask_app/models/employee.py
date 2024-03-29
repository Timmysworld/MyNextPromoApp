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
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.gs_level = data['gs_level']
        self.veteran = data['veteran']
        self.years_of_service = data['years_of_service']
        self.potential_hire = data['potential_hire']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.position  = None;
        self.certification = None;
        self.education_level = None;

    @classmethod
    def create_employee(cls,data):
        query = """
        INSERT INTO employees (first_name,last_name,email,gs_level,veteran,years_of_service,potential_hire,Education_level_id,account_id,position_id)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(gs_level)s,%(veteran)s,%(years_of_service)s,%(potential_hire)s,%(edu_level)s,%(account_id)s,%(position_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_employees(cls):
        query = """
        SELECT * FROM Employees
        JOIN accounts ON accounts.id = employees.account_id
        """
        results =  connectToMySQL(cls.db).query_db(query)
        # print(results)
        ListOfEmployees = []
        for i in results:
            e = {
                "id": i['id'],
                "first_name":  i['first_name'],
                "last_name":  i['last_name'],
                "email":  i['email'],
                "gs_level":  i['gs_level'],
                "veteran":  i['veteran'],
                "years_of_service":  i['years_of_service'],
                "potential_hire":  i['potential_hire'],
                "created_at":  i['created_at'],
                "updated_at":  i['updated_at'],
            }
            ListOfEmployees.append(cls(e))
        return ListOfEmployees
    
    @classmethod
    def get_employee(cls, id):
        data = {"id": id}
        query =  """
        SELECT * FROM Employees
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_all_positions(cls):
        query =""" 
        SELECT * FROM positions 
        JOIN Employees on positions.id = Employees.position_id
        """
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        ListOfPositions = []
        for p  in results: 
            ### Employee dictionary ###
            e = {
                "id": p['Employees.id'],
                "first_name":  p['first_name'],
                "last_name":  p['last_name'],
                "email":  p['email'],
                "gs_level":  p['gs_level'],
                "veteran":  p['veteran'],
                "years_of_service":  p['years_of_service'],
                "potential_hire":  p['potential_hire'],
                "created_at":  p['Employees.created_at'],
                "updated_at":  p['Employees.updated_at'],
            }
            ### passed employee diction and cast as employee  set as variable emp ###
            emp = Employee(e)
            pos = {
                "id": p['position_id'],
                "title": p['title'],
                "created_at":  p['created_at'],
                "updated_at":  p['updated_at'],
            }
            ### pass position dictionary  into emp with dot notation ###
            emp.position = pos
            ListOfPositions.append(emp) 
        return ListOfPositions
    
    def get_all_edu_level(cls,id):
        data = {"id": id}
        query =""" 
        SELECT * FROM edu_level 
        JOIN Employees on edu_level.id = Employees.edu_level_id
        """
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        ListOfEducation = []
        for edu  in results: 
            e = {
                "id": edu['Employees.id'],
                "first_name":  edu['first_name'],
                "last_name":  edu['last_name'],
                "email":  edu['email'],
                "gs_level":  edu['gs_level'],
                "veteran":  edu['veteran'],
                "years_of_service":  edu['years_of_service'],
                "potential_hire":  edu['potential_hire'],
                "created_at":  edu['Employees.created_at'],
                "updated_at":  edu['Employees.updated_at'],
            }
            emp = Employee(e)
            edu_level = {
                "id": edu['edu_level_id'],
                "name": edu['edu_level'],
                "created_at":  edu['created_at'],
                "updated_at":  edu['updated_at'],
            }

            emp.education_level = edu_level
            ListOfEducation.append(emp)
        return ListOfEducation

    

    @classmethod
    def update(cls, data):
        query = """
        UPDATE employee SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, 
        gs_level=%(gs_level)s, veteran=%(veteran)s,years_of_service=%(years_of_service)s,
        potential_hire=%(potential_hire)s,edu_level=%(edu_level)s,position_id=%(positions)s,
        updated_at=NOW() WHERE id = %(id)s;
        """ 
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete_employee(cls,id):
        data = {"id": id}
        query = "DELETE FROM employees WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results





















































































# [{'id': 1, 'first_name': 'johnny', 'last_name': 'Doe', 'email': 'jd@me.com', 'gs_level': 'gs_level', 'veteran': 1, 'years_of_service': 6, 'potential_hire': 0, 'created_at': datetime.datetime(2022, 11, 17, 20, 31), 'updated_at': datetime.datetime(2022, 11, 17, 20, 31), 'account_id': 2, 'Education_level_id': 4, 'accounts.id': 2, 'account_name': 'Schriever Fire', 'accounts.created_at': datetime.datetime(2022, 11, 17, 15, 51, 23), 'accounts.updated_at': datetime.datetime(2022, 11, 17, 15, 51, 23), 'admin_user_id': 2}]

    # @classmethod
    # def get_all_employees(cls):
    #     query="SELECT * FROM Employees"
    #     results=connectToMySQL(cls.db).query_db(query)
    #     return [cls(e) for e in results]

    # SELECT * FROM Employees
# JOIN accounts ON accounts.id = employees.account_id
# WHERE admin_user_id = 2

# -- INSERT INTO Education_levels (edu_level, value)
# -- VALUES ("some college",10)

# SELECT * FROM Education_levels

# @staticmethod
    # def validate_user():
    #     pass
        # INSERT INTO education_levels (edu_level)
        # VALUES (LAST_INSERT_ID(),%(edu_level)s);

        # INSERT INTO positions (title)
        # VALUES (LAST_INSERT_ID(),%(title)s);

        # INSERT INTO certifications (employee_id,name)
        # VALUES (LAST_INSERT_ID(),%(employee_id)s,%(name)s);
        
        # INSERT INTO other qualifications (certification)
        # VALUES (LAST_INSERT_ID()%(certification)s);

        # INSERT INTO collateral_duties (name)
        # VALUES (LAST_INSERT_ID(),%(name)s);