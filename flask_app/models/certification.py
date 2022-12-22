from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app  

class Certifications: 
    db = "MyNextPromoApp"
    def __init__(self,data):
        self.id = data['id'],
        self.name = data['name']

    @classmethod
    def get_all_certifications(cls):
        query ="""
        SELECT * FROM certifications
        """
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        ListOfCertifications = []
        for c in results:
            ListOfCertifications.append(cls(c))
        print(ListOfCertifications)
        # sends all certifications back to the html form to be looped
        return ListOfCertifications  

    #create the relationship and  insert  into employee has certification table 
    @classmethod
    def employee_cert_list(cls,data):
        query = f'INSERT into Employees_has_certifications (certification_id, Employee_id ) VALUES{data}'

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        return results



