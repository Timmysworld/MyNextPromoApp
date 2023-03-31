from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Collateral_Duties: 
    db = "MyNextPromoApp"
    def __init__(self,data):
        self.id = data['id'],
        self.name = data['name']

    @classmethod
    def get_all_collateral_duties(cls):
        query = """
        SELECT * FROM collateral_duties
        """
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        ListOfCollaterals =[]
        for cd in results:
            ListOfCollaterals.append(cls(cd))
        print(ListOfCollaterals)
        return ListOfCollaterals

    @classmethod
    def employee_cd_list(cls,data):
        query =f'INSERT into Employees_has_collateral_duties (collateral_duty_id,Employee_id) VALUES{data}'

        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        return results
    