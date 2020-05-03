from flask import Flask, render_template, request, make_response, redirect, url_for, session, send_from_directory
from datetime import datetime, date
from time import time
from werkzeug.utils import secure_filename
import os

from data import Data
import utils

app = Flask(__name__)
app.secret_key = "Very secret key"

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.config['UPLOAD_FOLDER'] = "uploads"

data = Data()

def render(template, **kwargs):
	return render_template(template + ".html", **kwargs)


def getRedirection(type):
	"""
	Returns the correct frontpage to redirect the user to for their user type.
	"""
	if type == utils.UserType.STUDENT:
		return redirect(url_for("index"))
	elif type == utils.UserType.TEACHER:
		return redirect(url_for("teacher"))
	elif type == utils.UserType.ADMINISTRATOR:
		return redirect(url_for("admin"))
	else:
		# Invalid user type
		return None

@app.route("/")
@app.route("/home")
def index():
	# Force user to log in if they are not logged in
	if not 'user' in session or session['user'] == None: 
		return redirect(url_for("login"))
	userdata = data.getUserData(session['user'])

	if userdata == None or not 'type' in userdata: # This should only happen on database wipes
		return redirect(url_for("login"))

	if userdata['type'] == utils.UserType.STUDENT:
		# Pass some variables and data functions
		return render("index", title="Forside", user=session['user'], userdata=userdata, data=data, utils=utils)
	else:
		return getRedirection(userdata['type'])

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		# Process login; G1
		
		username = request.values['username'].upper() # Uppercase because all usernames are generated to upper case.
		password = request.values['password']

		if(data.checkLogin(username, password)): # True if user-pass combination is valid
			# Send user to front page
			session['user'] = data.getUserIdFromName(username)
			return redirect(url_for("index"))
		else:
			# Failed to log in, indicate this to the user.
			print("User failed to log in")
			return render("login", title="Log ind", loginstatus="FAIL")
	else:
		return render("login", title="Log ind", loginstatus="NA")

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		# Proces registration; G2

		firstName = request.values['firstname']
		surnames = request.values['surnames']
		email = request.values['email']
		birthdate = request.values['birthdate']
		birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
		password = request.values['password']

		data.registerUser(firstName, surnames, email, birthdate, password)

		# Send user to front page
		return redirect(url_for("index"))
	else:
		return render("register", title="Registrer")

@app.route("/admin")
@app.route("/admin/<string:subpage>", methods=["GET", "POST"])
def admin(subpage="Admin Panel"):
	# Force user to log in if they are not logged in

	if not 'user' in session or session['user'] == None:
		return redirect(url_for("login"))
	
	userdata = data.getUserData(session['user'])

	if userdata['type'] != utils.UserType.ADMINISTRATOR:
		# Redirect the user to their correct front page if they are not admins
		return getRedirection(userdata['type'])

	# Template to show
	htmlpage = "/admin/" + (subpage.lower().replace(" ", ""))

	# Used for indicators after POST actions.
	status = "NEUTRAL"

	if request.method == "POST":
		# Now find out what form has been posted
		if "OPRET_KLASSEFAG" in request.form:
			status = opretKlassefag(request)
		elif "OPRET_KLASSE" in request.form:
			status = opretKlasse(request)
		elif "REDIGER_BRUGER" in request.form:
			status = redigerBruger(request)
		elif "REDIGER_KLASSE" in request.form:
			status = redigerKlasse(request)

	return render(htmlpage, subpage=subpage.title(), status=status, data=data, utils=utils)


@app.route("/teacher")
@app.route("/teacher/<string:subpage>", methods=["GET", "POST"])
def teacher(subpage="Lærer Panel"):
	# Force user to log in if they are not logged in

	if not 'user' in session or session['user'] == None:
		return redirect(url_for("login"))

	userdata = data.getUserData(session['user'])

	if userdata['type'] != utils.UserType.TEACHER:
		# Redirect the user to their correct front page if they are not admins
		return getRedirection(userdata['type'])

	# Template to show
	htmlpage = "/teacher/" + (subpage.lower().replace(" ", ""))

	# Used for indicators after POST actions.
	status = "NEUTRAL"

	# POST: A form has been submitted
	if request.method == "POST":
		# Now find out what form has been posted
		if "OPRET_OPGAVE" in request.form:
			status = opretOpgave(request)
		elif "OPRET_EMNE" in request.form:
			status = opretEmne(request)

	return render(htmlpage, user=userdata, subpage=subpage.title(), status=status, data=data, utils=utils)

@app.route("/subject/<idd>", methods=["GET", "POST"])
def subject(idd):
	"""
	Subject page for a student
	"""
	id = None
	status = "NEUTRAL"

	# Form has been submitted
	if request.method == "POST":
		print("POST",request)
		id = int(request.form['submitid'])
		if "AFLEVER" in request.form:
			status = submitAssignment(request)
		elif "SLET_AFLEVERING" in request.form:
			status = deleteAssignment(request)
	else:
		id = int(idd)

	# Get all data of the subject
	subject = data.getSubjectData(id)
	userdata = data.getUserData(session['user'])


	return render("/student/subject", status=status, userdata=userdata, subject=subject, utils=utils, data=data)

@app.route("/uploads/<path:filename>", methods=["GET", "POST"])
def download(filename):
	uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
	return send_from_directory(directory=uploads, filename=filename)

def opretKlasse(request):
	"""
	Handles the POST request where a class is to be created and returns the status
	"""

	# Name of the class
	name = request.form['name']

	# Graduation year of the class
	year = int(request.form['year'])

	# Line of studying of the class (StudyLine number)
	study = int(request.form['study'])

	# Students to be added to the class
	students = request.form.getlist("students")

	# Add the class to database and declare the class id
	classid = data.addClass(name, year, study)

	# Now change the selected student's classes to this class
	if students != None and len(students) > 0:
		for student in students:
			# Parse student id to int
			studentid = int(student)
			data.editUserClass(studentid, classid)
	
	return "SUCCESS"

def opretKlassefag(request):
	"""
	Handles the POST request where a class-subject is to be created and returns the status
	"""
	# Subject id
	subject = int(request.form['subject'])

	# Subject level
	level = int(request.form['level'])

	# Course hours
	hours = int(request.form['courseHours'])

	# Class
	clazz = int(request.form['class'])

	# Start date
	startDate = datetime.strptime(request.form['startDate'], "%Y-%m-%d").date()

	# End date
	endDate = datetime.strptime(request.form['endDate'], "%Y-%m-%d").date()

	# Add the class subject and declare the subject id
	subjectid = data.addSubject(subject, level, hours, clazz, startDate, endDate)

	# Update all students and link all class students to the new subject
	for student in data.getClassStudents(clazz):
		data.addUserSubject(student, subjectid)
	
	return "SUCCESS"

def redigerBruger(request):
	"""
	Handles the POST request where a user is to be changed, and returns the status.
	"""
	# Get all variables from the form
	userid = int(request.form['bruger'])
	username = request.form['username']
	firstName = request.form['firstname']
	surnames = request.form['surnames']
	email = request.form['email']
	birthdate = datetime.strptime(request.form['birthdate'], "%Y-%m-%d").date()
	clazz = int(request.form['class'])
	usertype = int(request.form['type'])

	# Change the user in database, and update their database relationships with other tables.
	data.editUser(userid, username, firstName, surnames, email, birthdate, clazz, usertype)
	data.updateUser(userid)

	return "SUCCESS"

def redigerKlasse(request):
	"""
	Handles the POST request where a user is to be changed, and returns the status.
	"""
	# Get all variables from the form
	classid = int(request.form['class'])
	classname = request.form['name']
	classyear = int(request.form['year'])
	classstudy = int(request.form['study'])

	# Update in database
	data.editClass(classid, classname, classyear, classstudy)

	return "SUCCESS"

def opretOpgave(request):
	"""
	Handles the POST request when a teacher adds a task.
	"""
	# Get the data from the form
	subject = int(request.form['subject'])
	topic = int(request.form['task-topic'])
	name = request.form['task-name']
	desc = request.form['task-description']
	hours = int(request.form['task-hours'])
	taskType = int(request.form['task-type'])
	date = datetime.strptime(request.form['task-date'], "%Y-%m-%dT%H:%M")

	print(request)
	print()
	print(request.form)
	
	# Add task to database
	data.addTask(name, desc, date, taskType, hours, subject, topic)

	return "SUCCESS"

def opretEmne(request):
	"""
	Handles the POST request when a teacher adds a topic.
	"""
	# Get data from the form
	subject = int(request.form['subject'])
	name = request.form['topic-name']
	desc = request.form['topic-description']

	# Add topic to database
	data.addTopic(name, subject, desc)

	return "SUCCESS"

def submitAssignment(request):
	file = request.files['file']
	task = request.form['submittask']

	filename = secure_filename(str(int(round(time()))) + "_" + file.filename)

	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	data.addTaskSubmission(session['user'], task, filename, datetime.now())

	return "SUCCESS"

def deleteAssignment(request):
	file = request.form['delete-file-id']
	filename = request.form['delete-file-name']
	
	# Remove file from database
	data.removeTaskSubmission(file)

	# Remove file from data system

	# Windows won't allow file deletion, so files are not deleted, but should be idealy.
	#path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	#os.chmod(path, 0o777)  # Enable file writing
	#os.remove(path)
	
	return "SUCCESS_DEL"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
