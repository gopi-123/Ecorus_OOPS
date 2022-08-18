# using flask_restful
from flask import Flask, jsonify, request, g, render_template
from flask_restful import Resource, Api
import sqlite3
from flask_bootstrap import Bootstrap

# creating the flask app
app = Flask(__name__)
#bootstrap = Bootstrap(app)



def connect_db():
	sql = sqlite3.connect('./database.db')
	sql.row_factory = sqlite3.Row
	return sql

def get_db():
    #Check if DB is there

    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db


#close the connection to the database automatically
@app.teardown_appcontext
def close_db(error):
	# if global object has a sqlite database then close it. 
	# If u leave it open no one can access it and gets lost in memory causing leaks.

	if hasattr(g,'sqlite_db'):
		g.sqlite3_db.close()




# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):

		return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number

@app.route('/users')
def get():
	#return {"Name": {self.name}, "Age": {self.age}}
	user_details = {
		'name': 'GAN',
		'age': 21
		}
		
	return render_template('test.html', user=user_details)

	#return render_template('index.html', name=current_user.username)
	#return {"Name": "Gan", "Age": 20}


# adding the defined resources along with their corresponding urls
#api.add_resource(Hello, '/')
#api.add_resource(Person, '/users')


# driver function
if __name__ == '__main__':
	app.run(debug = True)
