# using flask_restful
import sqlite3

from flask import Flask, Response, g, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_assignment_1 import Person

# creating the flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# creating an API object
api = Api(app)

def connect_db():
    
    print("1. Inside connect_db")
    conn = sqlite3.connect('database.db')
    return conn



# close the connection to the database automatically
@app.teardown_appcontext
def close_db(error):
    # if global object has a sqlite database then close it.
    # If u leave it open no one can access it and gets lost in memory causing leaks.

    print("3. Inside close_db")
    if hasattr(g, "sqlite_db"):
        g.sqlite3_db.close()


def create_db_table():
    # implements the person database

    try:
        conn = connect_db()
        #conn = get_db()
        cur = conn.cursor()
        sql_query = '''
        CREATE TABLE IF NOT EXISTS persons
        ( person_id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)
        '''
        cur.execute(sql_query)
        conn.commit()
        print("Person table created successfully")

    except:
        print("Person table creation failed")

    finally:
        conn.close()


def insert_person(person):
    # defines a function that adds a new user into the database
    print("***Inside insert_person:",person)

    inserted_person = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO persons (name, age) VALUES (?, ?)",
            (person["name"], person["age"]),
        )
        conn.commit()
        inserted_person = get_person_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_person

def get_persons():
    print("DB: inside get_persons persons ")
    persons = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            person = {}
            person["person_id"] = i["person_id"]
            person["name"] = i["name"]
            person["age"] = i["age"]
            persons.append(person)
            print("persons:", persons)

    except:
        persons = []

    return persons


def get_person_by_id(person_id):
    # implements the feature to retrieve user(s) from the database.

    person = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        person["person_id"] = row["person_id"]
        person["name"] = row["name"]
        person["age"] = row["age"]
    except:
        person = {}

    return person


class Index(Resource):

    def get(self):
        #return '<h1>Hello, World!</h1>'

        return Response('<h1>Hello, World!</h1>')


# another resource to calculate the square of a number
class Users(Resource):

    def get(self):

        # return {"Name": {self.name}, "Age": {self.age}}

        #user_details = {'name': 'GAN', 'age': 21}
        create_db_table()
        person = Person("ganga", 15)

        inserted_person = insert_person(person.__dict__)

        persons_list = get_persons()

        print("*** persons_list:", persons_list, len(persons_list))

        return Response(render_template('test.html',
                                result_user=persons_list, mimetype='text/html'))  

# adding the defined resources along with their corresponding urls
api.add_resource(Index, '/')
api.add_resource(Users, "/users")
#api.add_resource(Person, "/users")



# driver function
if __name__ == "__main__":
    app.run(debug=True)
