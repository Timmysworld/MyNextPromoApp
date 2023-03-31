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
    
    # @classmethod
    # def get_certification_by_id(cls,data):
    #     query = """

    #     SELECT certifications.id, certifications.name
    #     FROM Employees_has_certification
    #     INNER JOIN certifications  
    #     ON Employees_has_certification.certification_id = certifications.id
    #     INNER JOIN Employees 
    #     ON Employees_has_certification.employee_id = Employee.id
    #     WHERE Employees.id = %(id)s

    #     """
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     print(results)
    #     certlist= []
    #     for cert in results:
    #         one = {
    #             'id': cert['id'],
    #             'name': cert['name'],
    #             'created_at': "",
    #             'updated_at': ""
    #             }
    #         certlist.append(one)
    #     return certlist
    #create the relationship and  insert  into employee has certification table 
    @classmethod
    def employee_cert_list(cls,data):
        query = f'INSERT into Employees_has_certifications (certification_id, Employee_id ) VALUES{data}'

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        return results



