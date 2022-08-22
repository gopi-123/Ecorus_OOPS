from flask import Response, jsonify, render_template, request
from flask_restful import Resource
from office_table import (create_office_db_table, delete_employee_by_id,
                          get_office_data, insert_office)

"""
class OfficeData(Resource):
    
    def get(self):
        
        # return {Name:ecorus, People working:{'ganga': 15, 'eduardo': 0} }

        # return {'name': 'ecorus', 'people_working': {'ganga': 15, 'eduardo': 0}}

        
        eduardo = Person("eduardo")
        ganga = Person("ganga", 15)
        

        office_obj = Office("ecorus")
        
        print("*** INitatiing **", office_obj.__dict__)

        office_obj.start_working_for(eduardo)
        office_obj.start_working_for(ganga)

        office_obj.finished_working_for(eduardo)
        office_obj.finished_working_for(ganga)
        print("### office_obj.__dict_", office_obj.__dict__)
        

        create_office_db_table()
        inserted_office = insert_office(office_obj.__dict__)
       

        office_data_list = get_office_data()

        print("*** office_data_list:", office_data_list, len(office_data_list))

        return Response(render_template('office.html',
                                result_office=office_data_list, mimetype='text/html')) 
"""

class OfficeData(Resource):

    def __init__(self) -> None:
        print(" ### inside init__ of office_api_resource OfficeData")
        create_office_db_table()
    
    def get(self):

        office_data_list = get_office_data()

        print("*** office_data_list:", office_data_list, len(office_data_list))

        return Response(render_template('office.html',
                                result_office=office_data_list, mimetype='text/html'))


class OfficeStartWorkingFor(Resource):

    def __init__(self) -> None:
        print(" ### inside init__ of office_api_resource start-working-for")
        create_office_db_table()
        #super().__init__()
    
    def post(self):
        """
        create/add person working to office table
        """
        #Note you can either take data from implemented classes or from Postman Body in format
        # json format object= {  "name": "ecorus",  "people_working": { "shiva": 21  } }{  "name": "ecorus",  "people_working": { "shiva": 21  } }
        office_dict = request.get_json()    

        return Response(render_template('officecreated.html',
                                result_office=insert_office(office_dict), mimetype='text/html'))

class OfficeFinishedWorkingFor(Resource):

    def __init__(self) -> None:
        print(" ### inside init__ of office_api_resource start-working-for")
        create_office_db_table()
    
    def delete(self, employee_id):
        """
        Delete reocrd from office table by removing person/employee from people_working
        """
        
        message_dict = delete_employee_by_id(employee_id)
        print("\n message dict:", message_dict)
        if message_dict["status"] == "Employee deleted successfully":
            office_data_list = get_office_data()
            return Response(render_template('office.html',
                                    result_office=office_data_list, mimetype='text/html'))

        else:
            return jsonify(message_dict)
