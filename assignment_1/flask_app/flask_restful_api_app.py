# using flask_restful
import sqlite3

from flask import Flask, Response, g, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_restful import Api, Resource

# creating the flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)

# creating an API object
api = Api(app)


def connect_db():
    sql = sqlite3.connect("./database.db")
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    # Check if DB is there

    if not hasattr(g, "sqlite3"):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db


# close the connection to the database automatically
@app.teardown_appcontext
def close_db(error):
    # if global object has a sqlite database then close it.
    # If u leave it open no one can access it and gets lost in memory causing leaks.

    if hasattr(g, "sqlite_db"):
        g.sqlite3_db.close()


def create_db_table():
    # implements the person database

    try:
        conn = connect_db()
        cur = conn.cursor()
        sql_query = "CREATE TABLE persons"
        "( person_id INTEGER PRIMARY KEY NOT NULL,"
        "name TEXT NOT NULL,"
        "age INTEGER NOT NULL;)"
        cur.execute(sql_query)
        conn.commit()
        print("Person table created successfully")

    except:
        print("Person table creation failed")

    finally:
        conn.close()


def insert_person(person):
    # defines a function that adds a new user into the database

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


def update_person(person):
    # implements the feature to retrieve user(s) from the database.

    updated_person = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE persons SET name = ?, age = ? WHERE person_id =?",
            (person["name"], person["age"]),
        )
        conn.commit()
        # return the user
        updated_person = get_person_by_id(person["person_id"])

    except:
        conn.rollback()
        updated_person = {}
    finally:
        conn.close()

    return updated_person


def delete_person(person_id):
    # implements the delete user feature

    message = {}
    try:
        conn = connect_db()
        conn.execute("DELETE from users WHERE user_id = ?", (person_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return jsonify({"message": "hello world"})

    # Corresponds to POST request
    def post(self):

        data = request.get_json()  # status code
        return jsonify({"data": data}), 201


# another resource to calculate the square of a number
class Person(Resource):

    def get(self):

        # return {"Name": {self.name}, "Age": {self.age}}

        user_details = {'name': 'GAN', 'age': 21}

        return Response(render_template('test.html',
                        result_user=user_details, mimetype='text/html'))


# adding the defined resources along with their corresponding urls
# api.add_resource(Hello, '/')
api.add_resource(Person, "/users")

# driver function
if __name__ == "__main__":
    app.run(debug=True)
