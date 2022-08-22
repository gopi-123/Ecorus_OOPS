# using flask_restful
import sqlite3

from flask import Flask, Response, g, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_assignment_1 import Person, Office
from persons_table import create_persons_db_table, insert_person, get_persons, get_person_by_id, update_person_name, update_birthday_age
from office_table import create_office_db_table, insert_office, get_office_data, get_office_by_id
from office_api_resource import OfficeData, OfficeStartWorkingFor, OfficeFinishedWorkingFor

# creating the flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# creating an API object
api = Api(app)

"""
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("name", type=str, help="name is required", required=True)
task_post_args.add_argument("age", type=int, help="age is required", required=True)
"""

# close the connection to the database automatically
@app.teardown_appcontext
def close_db(error):
    # if global object has a sqlite database then close it.
    # If u leave it open no one can access it and gets lost in memory causing leaks.

    print("3. Inside close_db")
    if hasattr(g, "sqlite_db"):
        g.sqlite3_db.close()

class Index(Resource):

    def get(self):
        #return '<h1>Hello, World!</h1>'

        return Response('<h1>Hello, World!</h1>')


class Users(Resource):

    def __init__(self) -> None:
        print(" ### inside init__ of USERs")
        create_persons_db_table()

    def get(self):
        # retrieves all person records

        print("### INSIDE NEW GET ###")
        persons_list = get_persons()

        return Response(render_template('person.html',
                        result_user=persons_list, mimetype='text/html'))

    def post(self):
        # create / add person to the person table

        # args = task_post_args.parse_args()
        # todos[todo_id] = request.form['data']
        person_dict = request.get_json()
        
        #return jsonify(insert_person(person))
        return Response(render_template('createdperson.html', 
                                result_dict=insert_person(person_dict), mimetype='text/html'))


    
    def get_old(self):

        # return {"Name": {self.name}, "Age": {self.age}}

        # user_details = {'name': 'GAN', 'age': 21}

        person = Person("GAN", 15)
        
        create_persons_db_table()
        inserted_person = insert_person(person.__dict__)

        persons_list = get_persons()

        print("*** persons_list:", persons_list, len(persons_list))

        return Response(render_template('person.html',
                                result_user=persons_list, mimetype='text/html'))  
                                

class ChangeUserName(Users, Resource):

    def __init__(self) -> None:
        print("##inside super__init")
        super().__init__()
    
    def put(self):
        person_dict = request.get_json()
        
        #return jsonify(insert_person(person))
        return Response(render_template('changename.html', 
                                result_dict=update_person_name(person_dict), mimetype='text/html'))


class HappyBirthday(Users, Resource):

    def __init__(self) -> None:
        print("##inside super__init")
        super().__init__()
    
    def put(self):
        person_dict = request.get_json()
        
        #return jsonify(insert_person(person))
        return Response(render_template('birthday.html', 
                                result_dict=update_birthday_age(person_dict), mimetype='text/html'))

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

# adding the defined resources along with their corresponding urls
"""
api.add_resource(Index, '/')
api.add_resource(Users, "/api/users")
api.add_resource(ChangeUserName, "/api/users/change-person-name")
api.add_resource(HappyBirthday, "/api/users/happy-birthday")
"""

api.add_resource(OfficeData, "/api/office")
api.add_resource(OfficeStartWorkingFor, "/api/office/add/start-working-for")

api.add_resource(OfficeFinishedWorkingFor, "/api/office/remove/finished_working_for/<int:employee_id>")

# api.add_resource(Person, "/users")



# driver function
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
