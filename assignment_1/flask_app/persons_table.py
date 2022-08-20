
import sqlite3

from flask import g, jsonify


def connect_db():
    
    print("1. Inside connect_db")
    conn = sqlite3.connect('database.db')
    return conn

def create_persons_db_table():
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

    except sqlite3.DatabaseError:
        print("Person table creation failed")

    finally:
        conn.close()


def insert_person(person):
    # defines a function that adds a new user into the database
    print("***Inside insert_person:", person)

    inserted_person = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO persons (name, age) VALUES (?, ?)",
            (person["name"], person["age"])
        )
        conn.commit()
        inserted_person = get_person_by_id(cur.lastrowid)
    except sqlite3.DatabaseError:
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

    except sqlite3.DatabaseError:
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
    except sqlite3.DatabaseError:
        person = {}

    return person
