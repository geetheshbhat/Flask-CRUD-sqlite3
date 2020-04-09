# Flask-CRUD-sqlite3
A simple Flask Server for performing CRUD operations on Database using REST API

# What does this application do?
It performs 
- 	Create:
- 	Read:
-	Update: 
-	Delete

# How will I run this appliction?
Install Flask and run the application using `python app.py`. You have to use Postman to send request

# Example:

GET ` http://127.0.0.1:5000/read `

POST `http://127.0.0.1:5000/create/<movie name>`

PUT `http://127.0.0.1:5000/update`
	
	JSON {
	"old_name":"Harry Potter",
	"new_name":"Harry"
	}

DELETE `http://127.0.0.1:5000/delete/Harry`
