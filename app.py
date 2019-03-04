from flask import Flask, render_template,request,flash,session
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database_setup import *

app = Flask(__name__)
app.debug = True
Base = declarative_base()
# Connect to database
engine = create_engine('sqlite:///student.db')
Base.metadata.bind = engine
# Create session
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
	return render_template("homepage.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

"""@app.route('/lists')
def index():
	return render_template("lists.html")
"""
@app.route('/list1')
def list1():
	return render_template("link1.html")

@app.route('/list2')
def list2():
	return render_template("link2.html")

@app.route('/list3')
def list3():
	return render_template("link3.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
	if request.method == 'POST':
		newitem = User(
		id = request.form['id'],
		name = request.form['name'],
		email = request.form['email'],
		password = request.form['password'] )
		session.add(newitem)
		session.commit()
		# flash('record added successfully')
		return render_template("signup.html")
		flash('record added successfully')
	else:
		flash('You were successfully logged in')
		return render_template("signup.html")	
    
@app.route('/signin')
def signin():
	return render_template("signin.html")
if __name__ == '__main__':
	app.secret_key = 'APP_SECRET_KEY'
	app.run()