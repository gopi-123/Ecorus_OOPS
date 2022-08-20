# using flask_restful
import sqlite3

from flask import Flask, Response, g, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_assignment_1 import Person, Office
from persons_table import create_persons_db_table, insert_person, get_persons, get_person_by_id
from office_table import create_office_db_table, insert_office, get_office_data, get_office_by_id

# creating the flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# creating an API object
api = Api(app)

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


# another resource to dispaly the Persons inforamtion
class Users(Resource):

    def get(self):

        # return {"Name": {self.name}, "Age": {self.age}}

        # user_details = {'name': 'GAN', 'age': 21}
        
        person = Person("ganga", 15)
        
        create_persons_db_table()
        inserted_person = insert_person(person.__dict__)

        persons_list = get_persons()

        print("*** persons_list:", persons_list, len(persons_list))

        return Response(render_template('person.html',
                                result_user=persons_list, mimetype='text/html'))  


class OfficeData(Resource):
    
    def get(self):
        
        # return {Name:ecorus, People working:{'ganga': 15, 'eduardo': 0} }

        # return {'name': 'ecorus', 'people_working': {'ganga': 15, 'eduardo': 0}}

        
        eduardo = Person("eduardo")
        ganga = Person("ganga", 15)

        office_obj = Office("ecorus")

        print("*** INitatiing **",office_obj.__dict__)

        office_obj.start_working_for(eduardo)
        office_obj.start_working_for(ganga)
        
        office_obj.finished_working_for(eduardo)
        # office_obj.finished_working_for(ganga)

        create_office_db_table()
        inserted_office = insert_office(office_obj.__dict__)

        office_data_list = get_office_data()

        print("*** office_data_list:", office_data_list, len(office_data_list))

        return Response(render_template('office.html',
                                result_office=office_data_list, mimetype='text/html')) 



# adding the defined resources along with their corresponding urls
api.add_resource(Index, '/')
api.add_resource(Users, "/users")
api.add_resource(OfficeData, "/office")

# api.add_resource(Person, "/users")



# driver function
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
