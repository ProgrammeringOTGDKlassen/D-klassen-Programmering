import sqlite3
import random
import bcrypt
import datetime
import utils

class Data:

	def __init__(self):
		self.con = sqlite3.connect("otgintra.db")

		self.initializeTables()
	
	def openConnection(self):
		self.con = sqlite3.connect("otgintra.db")
	
	def closeConnection(self):
		self.con.close()

	def initializeTables(self):
		sql = """CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, surnames TEXT, email TEXT, birthdate DATE, password TEXT, salt TEXT, class INTEGER, type INTEGER);
				 CREATE TABLE IF NOT EXISTS classes(id INTEGER PRIMARY KEY, name TEXT, year INTEGER, line_of_study INTEGER);
				 CREATE TABLE IF NOT EXISTS exams(id INTEGER PRIMARY KEY, subject INTEGER, level INTEGER, date TIMESTAMP);
				 CREATE TABLE IF NOT EXISTS user_grades(id INTEGER PRIMARY KEY, user INTEGER, subject INTEGER, date DATE, grade INTEGER, grade_type INTEGER, released BOOL);
				 CREATE TABLE IF NOT EXISTS grade_dates(id INTEGER PRIMARY KEY, grading_date TIMESTAMP, release_date TIMESTAMP);
				 CREATE TABLE IF NOT EXISTS user_subjects(id INTEGER PRIMARY KEY, user INTEGER, subject INTEGER);
				 CREATE TABLE IF NOT EXISTS absence(id INTEGER PRIMARY KEY, user INTEGER, module INTEGER, absence INTEGER);
				 CREATE TABLE IF NOT EXISTS subjects(id INTEGER PRIMARY KEY, subject INTEGER, level INTEGER, course_hours INTEGER, class INTEGER, start_date DATE, end_date DATE);
				 CREATE TABLE IF NOT EXISTS modules(id INTEGER PRIMARY KEY, start_date TIMESTAMP, end_date TIMESTAMP, subject INTEGER);
				 CREATE TABLE IF NOT EXISTS topics(id INTEGER PRIMARY KEY, name TEXT, subject INTEGER, description TEXT);
				 CREATE TABLE IF NOT EXISTS user_modules(id INTEGER PRIMARY KEY, user INTEGER, module INTEGER);
				 CREATE TABLE IF NOT EXISTS material(id INTEGER PRIMARY KEY, subject INTEGER, topic INTEGER, file_name TEXT);
				 CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, name TEXT, description TEXT, date TIMESTAMP, type INTEGER, work_hours INTEGER, subject INTEGER, topic INTEGER);
				 CREATE TABLE IF NOT EXISTS marks(id INTEGER PRIMARY KEY, submission INTEGER, description TEXT, file_name TEXT);
				 CREATE TABLE IF NOT EXISTS task_files(id INTEGER PRIMARY KEY, task INTEGER, file_name TEXT);
				 CREATE TABLE IF NOT EXISTS task_submissions(id INTEGER PRIMARY KEY, user INTEGER, task INTEGER, file_name TEXT, date TIMESTAMP);"""
		for cmd in sql.split(";"): # Too lazy to split up in strings
			self.con.execute(cmd)
		self.con.commit()
		self.closeConnection()
	
	def registerUser(self, firstName, surnames, email, birthdate, password):
		"""
		Register a new user to the database.
		"""
		username = (firstName[0] + surnames[0] + str(random.randint(10000,99999))).upper()

		salt = bcrypt.gensalt()
		hashedPassword = bcrypt.hashpw(password.encode(), salt)

		sql = "INSERT INTO users(username, first_name, surnames, email, birthdate, password, salt, class, type) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (username, firstName, surnames, email, birthdate, hashedPassword, salt, 0, 0))  # 0 for linked class

		self.con.commit()
		self.closeConnection()
	
	def getUsers(self):
		"""
		Returns all users in the database.
		"""
		sql = "SELECT * FROM users"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql)

		users = c.fetchall()

		self.closeConnection()

		if len(users) < 1: # No users found
			return []
		
		res = []
		for user in users:
			dic = {
				'id': int(user[0]),
				'username': user[1],
				'firstname': user[2],
				'surnames': user[3],
				'email': user[4],
				'birthdate': datetime.datetime.strptime(user[5], "%Y-%m-%d").date(),
				# Skipping password details
				'class': int(user[8]),
				'type': int(user[9])
			}
			res.append(dic)

		return res
	
	def editUser(self, userid, username, firstName, surnames, email, birthdate, clazz, usertype):
		"""
		Changes a user in the database
		"""
		sql = "UPDATE users SET username=?,first_name=?,surnames=?,email=?,birthdate=?,class=?,type=? WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (username,firstName,surnames,email,birthdate,clazz,usertype,userid))
		self.con.commit()

		self.closeConnection()
	

	# Has not been tested TODO
	def updateUser(self, user):
		"""
		Updates a user in the database; mainly used to update students' subjects and modules.
		"""
		# TODO update user modules

		# First wipe all class subjects that the user is linked to
		sqlDelete = """DELETE FROM user_subjects us
		INNER JOIN subjects s ON us.subject=s.id
		WHERE us.user=? AND s.class!=0
		"""

		sqlDelete = """ DELETE FROM user_subjects
		WHERE user=? AND subject IN (SELECT id FROM subjects WHERE class!=0)

		"""

		self.openConnection()

		self.con.execute(sqlDelete, (user,))
		

		# Now select all subjects of the user's class in order to update user_subjects.
		sqlSelect = """SELECT * FROM subjects s
		INNER JOIN users u ON s.class=u.class
		WHERE u.id=?
		"""
		
		c = self.con.cursor()
		c.execute(sqlSelect, (user,))

		subjects = c.fetchall()

		# Now add the subjects to user_subjects
		for subject in subjects:
			c.execute("INSERT INTO user_subjects(user, subject) VALUES(?, ?)", (user, subject[0]))

		self.con.commit()

		self.closeConnection()

	
	def checkLogin(self, username, password):
		"""
		Checks username and password up against the database. Returns true if the username-password combination is valid.
		"""
		sql = "SELECT password FROM users WHERE username=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (username,))

		result = c.fetchall()
		
		self.closeConnection()

		if len(result) < 1: # The given username doesn't exist in the database.
			return False
		
		dbHashedPassword = result[0][0]
		
		return bcrypt.checkpw(password.encode(), dbHashedPassword)
	
	def getUserIdFromName(self, username):
		"""
		Returns the id of the user with the specified username or None if it's invalid
		"""
		username = username.upper() # Uppercase because all generated usernames are upper case.

		sql = "SELECT id FROM users WHERE username=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (username,))

		result = c.fetchall()

		self.closeConnection()

		if len(result) < 1: # Nothing found, return None
			return None
		
		return result[0][0] # Return the id.

	def getClasslessUsers(self):
		"""
		Returns all the users that don't have a class
		"""
		sql = "SELECT * FROM users where class=0 AND type=0"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql)

		students = c.fetchall()

		if len(students) < 1: # No classless students
			return []

		res = []
		for student in students:
			# Only return id, username, and name; nothing else is needed
			dic = {
				'id': int(student[0]),
				'username': student[1],
				'name': student[2] + " " + student[3], # Full name
			}
			res.append(dic)
		
		return res


	def getUserData(self, id):
		"""
		Returns all of the data (as a tuple) of a user with the specified id, or None if it's invalid.
		"""
		sql = "SELECT * FROM users WHERE id=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (id,))

		result = c.fetchall()

		self.closeConnection()

		if len(result) < 1: # Invalid id
			return None

		# Now load the user's subjects:
		sql = "SELECT * FROM user_subjects WHERE user=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (id,))

		subjResult = c.fetchall()

		subjects = []
		for subject in subjResult:
			subjId = subject[2]

			# Now query for each subject
			sql = "SELECT * FROM subjects WHERE id=?"

			c = self.con.cursor()
			c.execute(sql, (subjId,))

			subjData = c.fetchone()

			# Check if the subject is still active
			now = datetime.date.today()
			startDate = datetime.datetime.strptime(subjData[5], "%Y-%m-%d").date()
			endDate = datetime.datetime.strptime(subjData[6], "%Y-%m-%d").date()

			active = now <= endDate

			data = {
				'id': int(subjId),
				'subject': utils.Subject.name(subjData[1]),
				'level': utils.SubjectLevel.name(int(subjData[2])),
				'courseHours': int(subjData[3]),
				'class': int(subjData[4]),
				'startDate': startDate,
				'endDate': endDate,
				'active': active
			}
			subjects.append(data)

		self.closeConnection()

		# (id, username, firstname, surnames, email, birthdate, class, subjects)
		userdata = {
			'id': id,
			'username': result[0][1],
			'firstname': result[0][2],
			'surnames': result[0][3],
			'email': result[0][4],
			'birthdate': datetime.datetime.strptime(result[0][5], "%Y-%m-%d").date(),
			# Not passing through password and salt, as they won't be used.
			'class': int(result[0][8]),
			'type': int(result[0][9]),
			'subjects': subjects
		}
		return userdata
	
	def getUserTasks(self, user):
		"""
		Returns all assignemnts that the user is linked to, ordered in ascending date (oldest assignemnts first)
		"""
		# Select all tasks where the task and the user has a common 'subject' id linked using INNER JOIN.
		taskSql = """
		SELECT * FROM tasks t
		INNER JOIN user_subjects us ON t.subject=(SELECT us.subject WHERE us.user=?)
		WHERE us.user=?
		ORDER BY date ASC
		"""

		# Now obtain all the tasks
		self.openConnection()

		c = self.con.cursor()
		c.execute(taskSql, (user, user))

		tasks = c.fetchall()

		self.closeConnection()

		if len(tasks) < 1: # No tasks
			return []

		# Now parse the types and make it properly formatted with a list of dictionaries
		res = []
		for task in tasks:
			dic = {
				'id': int(task[0]),
				'name': task[1],
				'description': task[2],
				'date': datetime.datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S"),
				'type': int(task[4]),
				'workHours': int(task[5]),
				'subject': int(task[6]),
				'topic': int(task[7])
			}
			res.append(dic)

		return res
	
	def getUserLateAssignments(self, user):
		"""
		Returns the tasks passed submission deadlinethat the user has not submitted yet.
		"""
		# Get all tasks
		tasks = self.getUserTasks(user)

		# List of all late assignments
		res = []

		self.openConnection()

		c = self.con.cursor()

		now = datetime.datetime.now()
		for task in tasks:
			if task['type'] == utils.TaskType.SUBMISSION and task['workHours'] > 0: # Only task submissions can be late
				deadline = task['date']
				if now > deadline: # If deadline has already passed, we check if the student has submitted their assignment
					c.execute("SELECT * FROM task_submissions WHERE user=? AND task=?", (user, task['id']))
					if len(c.fetchall()) < 1: # No recorded assignment of that task
						res.append(task)
		
		self.closeConnection()

		return res

	def getUserSubmittedAssignments(self, user):
		"""
		Returns the assignments tasks that the user has submitted
		"""
		# Get all tasks where user and task has a common task submission
		sql = """
		SELECT * FROM tasks t 
		INNER JOIN task_submissions ts ON t.id=ts.task
		WHERE ts.user=?
		ORDER BY date DESC
		"""

		self.openConnection()

		c = self.con.cursor()		
		c.execute(sql, (user,))

		tasks = c.fetchall()

		self.closeConnection()

		if len(tasks) < 1: # No submissions
			return []
		

		# Now parse the types and make it properly formatted with a list of dictionaries
		res = []
		for task in tasks:
			dic = {
				'id': int(task[0]),
				'name': task[1],
				'description': task[2],
				'date': datetime.datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S"),
				'type': int(task[4]),
				'workHours': int(task[5]),
				'subject': int(task[6]),
				'topic': int(task[7])
			}
			res.append(dic)
		
		return res
	
	def getUserScheduledAssignments(self, user, taskType, workHours):
		"""
		Returns the upcoming assignments with the given task type for the given user.\nworkHours: Boolean (True = workHours > 0, False = workHours == 0)
		"""
		# Get all the tasks
		tasks = self.getUserTasks(user)

		# Filter tasks using method parameters
		res = []

		now = datetime.datetime.now()
		for task in tasks:
			deadline = task['date']
			if deadline <= now: # If deadline already passed we go to the next task.
				continue
			if task['type'] == taskType: # Types match
				if workHours: # Tasks should have work hours
					if task['workHours'] > 0:
						res.append(task)
				else: # Tasks should not have work hours
					if task['workHours'] <= 0:
						res.append(task)
		return res
	
	def getUserLateSubmissions(self, user):
		"""
		Returns all tasks that the user has submitted after the submission deadline.
		"""
		# All tasks with submission date later than the task deadline and with the user id.
		sql = """
		SELECT * FROM tasks t
		INNER JOIN task_submissions ts ON t.id=ts.task
		WHERE t.date < ts.date AND ts.user=?
		"""
		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (user,))

		tasks = c.fetchall()

		self.closeConnection()

		if len(tasks) < 1: # No late tasks! Great
			return []
		
		# Now parse the types and make it properly formatted with a list of dictionaries
		res = []
		for task in tasks:
			dic = {
				'id': int(task[0]),
				'name': task[1],
				'description': task[2],
				'date': datetime.datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S"),
				'type': int(task[4]),
				'workHours': int(task[5]),
				'subject': int(task[6]),
				'topic': int(task[7])
			}
			res.append(dic)

		return res

	def getUserReadingTasks(self, user):
		"""
		Returns a list of all the user's tasks with the task type set to "Read".
		"""
		taskSql = """
		SELECT * FROM tasks t
		INNER JOIN user_subjects us ON t.subject=(SELECT us.subject WHERE us.user=?)
		WHERE us.user=? AND t.type=0
		ORDER BY date ASC
		"""

		# Now obtain all the tasks
		self.openConnection()

		c = self.con.cursor()
		c.execute(taskSql, (user, user))

		tasks = c.fetchall()

		self.closeConnection()

		if len(tasks) < 1:  # No tasks
			return []

		# Now parse the types and make it properly formatted with a list of dictionaries
		res = []
		for task in tasks:
			dic = {
				'id': int(task[0]),
				'name': task[1],
				'description': task[2],
				'date': datetime.datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S"),
				'type': int(task[4]),
				'workHours': int(task[5]),
				'subject': int(task[6]),
				'topic': int(task[7])
			}
			res.append(dic)

		return res

	def addUserSubject(self, user, subject):
		"""
		Adds a relation between a user and a subject to the database.
		"""
		sql = "INSERT INTO user_subjects(user, subject) VALUES(?, ?)"

		self.openConnection()

		self.con.execute(sql, (user, subject))

		self.con.commit()
		self.closeConnection()
	
	def removeUserSubject(self, user, subject):
		"""
		Removes a relation between a user and a subject to the database.
		"""
		sql = "DELETE * FROM user_subjects WHERE user=? AND subject=?"

		self.openConnection()

		self.con.execute(sql, (user, subject))

		self.con.commit()
		self.closeConnection()
	
	def addUserModule(self, user, module):
		"""
		Adds a relation between a user and a module to the database.
		"""
		sql = "INSERT INTO user_modules(user, module) VALUES(?, ?)"

		self.openConnection()

		self.con.execute(sql, (user, module))

		self.con.commit()
		self.closeConnection()
	
	def removeUserModule(self, user, module):
		"""
		Removes a relation between a user and a module to the database.
		"""
		sql = "DELETE * FROM user_modules WHERE user=? AND module=?"

		self.openConnection()

		self.con.execute(sql, (user, module))

		self.con.commit()
		self.closeConnection()
	
	def addUserGrade(self, user, subject, date, grade, type):
		"""
		Links a grade to a user to the database.
		"""
		sql = "INSERT INTO user_grades(user, subject, date, grade, grade_type, released) VALUES(?, ?, ?, ?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (user, subject, date, grade, type, False)) # Default to not released

		self.con.commit()
		self.closeConnection()
	
	def editUserGrade(self, id, date=None, grade=None, type=None, released=None):
		"""
		Changes a grade for a user in the database.
		"""
		if date == None and grade == None and type == None and released == None:
			# Do nothing if there are no changed values
			return

		t = tuple()

		sql = "UPDATE user_grades SET "
		if date != None:
			sql += "date=?,"
			t = (*t, date)
		if grade != None:
			sql += "grade=?,"
			t = (*t, grade)
		if type != None:
			sql += "grade_type=?,"
			t = (*t, type)
		if released != None:
			sql += "released=?,"
			t = (*t, released)

		t = (*t, id)

		# Cut off the comma and add the rest
		sql = sql[0:len(sql)-2] + " WHERE id=?"

		self.openConnection()
		
		self.con.execute(sql, t)
		self.con.commit()

		self.closeConnection()
	
	def addGradeDate(self, gradingDate, receiveDate):
		"""
		Adds a grade date to the database.
		"""
		sql = "INSERT INTO grade_dates(grading_date, receive_date) VALUES(?, ?)"

		self.openConnection()

		self.con.execute(sql, (gradingDate, receiveDate))

		self.con.commit()
		self.closeConnection()

	def removeGradeDate(self, id):
		"""
		Removes a grade date from the database.
		"""
		sql = "DELETE * FROM grade_dates WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()

	def editGradeDate(self, id, gradingDate, receiveDate):
		"""
		Edits a grade date in the database.
		"""
		sql = "UPDATE grade_dates SET grading_date=?,receive_date=? WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (gradingDate, receiveDate, id))

		self.con.commit()
		self.closeConnection()

	def addTask(self, name, description, date, type, workHours, subject, topic):
		"""
		Adds a task to the database.
		"""
		sql = "INSERT INTO tasks(name, description, date, type, work_hours, subject, topic) VALUES(?,?,?,?,?,?,?)"

		self.openConnection()

		self.con.execute(sql, (name, description, date, type, workHours, subject, topic))

		self.con.commit()
		self.closeConnection()
	
	def removeTask(self, id):
		"""
		Removes a task from the database if it exists.
		"""
		sql = "DELETE * FROM tasks WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()
	
	def addTaskFile(self, task, fileName):
		"""
		Links a file to a task in the database.
		"""
		sql = "INSERT INTO task_files(task, file_name) VALUES(?, ?)"

		self.openConnection()

		self.con.execute(sql, (task, fileName))

		self.con.commit()
		self.closeConnection()
	
	def removeTaskFile(self, id):
		"""
		Removes a task file from the database.
		"""
		sql = "DELETE * FROM task_files WHERE id=?"

		self.openConnection()
		
		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()
	
	def addTaskSubmission(self, user, task, fileName, date):
		"""
		Adds a task submission to the database.
		"""
		sql = "INSERT INTO task_submissions(user, task, file_name, date) VALUES (?, ?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (user, task, fileName, date))

		self.con.commit()
		self.closeConnection()

	def removeTaskSubmission(self, id):
		"""
		Removes a task submission from the database.
		"""
		sql = "DELETE FROM task_submissions WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()

	def getTaskSubmission(self, user, task):
		"""
		Get the file information a user's task submission
		"""
		sql = "SELECT * FROM task_submissions WHERE task=? AND user=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (task, user))

		res = c.fetchall()

		if len(res) < 1: # No uploads
			return []
	
		files = []

		for f in res:
			dic = {
				'id': int(f[0]),
				'user': int(f[1]),
				'task': int(f[2]),
				'filename': f[3],
				'date': datetime.datetime.strptime(f[4], "%Y-%m-%d %H:%M:%S.%f")
			}
			files.append(dic)

		return files

	def registerAbsence(self, user, module, absence):
		"""
		Registers student absence to the database.
		"""
		sql = "INSERT INTO absence(user, module, absence) VALUES(?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (user, module, absence))

		self.con.commit()
		self.closeConnection()
	
	def editAbsence(self, id, absence):
		"""
		Edits student absence in the database.
		"""
		sql = "UPDATE absence SET absence=? WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (absence, id))
		
		self.con.commit()
		self.closeConnection()
	
	def addMaterial(self, subject, topic, fileName):
		"""
		Adds material to the database.
		"""
		sql = "INSERT INTO material(subject, topic, file_name) VALUES(?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (subject, topic, fileName))

		self.con.commit()
		self.closeConnection()

	def removeMaterial(self, id):
		"""
		Removes material from the database.
		"""
		sql = "DELETE * FROM material WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()
	
	def addMark(self, submission, description, file=None):
		"""
		Adds a mark to a submission to the database.
		"""
		sql = "INSERT INTO marks(submission, description, file) VALUES(?, ?, ?)"

		self.openConnection()
		
		self.con.execute(sql, (submission, description, file))
		
		self.con.commit()
		self.closeConnection()

	def removeMark(self, id):
		"""
		Removes a mark from the database.
		"""
		sql = "DELETE * FROM marks WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()

	def editMark(self, id, description, file):
		"""
		Edits the mark in the database.
		"""
		sql = "UPDATE marks SET description=?,file=? WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (description, file, id))

		self.con.commit()
		self.closeConnection()
	
	def addModule(self, startDate, endDate, subject):
		"""
		Adds a module to the database.
		"""
		sql = "INSERT INTO modules(start_date, end_date, subject) VALUES(?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (startDate, endDate, subject))

		self.con.commit()
		self.closeConnection()

	def removeModule(self, id):
		"""
		Removes a module from the database if it exists.
		"""
		sql = "DELETE * FROM modules WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()
	
	def addSubject(self, subject, level, courseHours, clazz, startDate, endDate):
		"""
		Adds a subject to the database.
		"""
		sql = "INSERT INTO subjects(subject, level, course_hours, class, start_date, end_date) VALUES(?, ?, ?, ?, ?, ?)"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (subject, level, courseHours, clazz, startDate, endDate))
		
		subjectid = c.lastrowid

		self.con.commit()
		self.closeConnection()

		return subjectid
	
	def getSubjects(self):
		"""
		Returns all subjects in a list.
		"""
		sql = "SELECT * FROM subjects"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql)

		subjects = c.fetchall()

		res = []

		if len(subjects) < 1: # No subjects
			return res
		
		for subject in subjects:
			now = datetime.date.today()
			startDate = datetime.datetime.strptime(subject[5], "%Y-%m-%d").date()
			endDate = datetime.datetime.strptime(subject[6], "%Y-%m-%d").date()

			active = now <= endDate

			data = {
				'id': int(subject[0]),
				'subject': utils.Subject.name(subject[1]),
				'level': utils.SubjectLevel.name(int(subject[2])),
				'courseHours': int(subject[3]),
				'class': int(subject[4]),
				'startDate': startDate,
				'endDate': endDate,
				'active': active
			}
			res.append(data)

		return res

	
	def getSubjectTeacher(self, subject):
		# TODO TODO TODO Optimize sql with Inner Join to avoid the for-loop
		"""
		Returns the user id of the teacher of the specified subject if there are any teachers, otherwise None.
		"""
		sql = "SELECT * FROM user_subjects WHERE subject=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (subject,))

		result = c.fetchall()

		if len(result) < 1: # No results
			return None
		
		for user in result:
			userid = user[1]
			sql = "SELECT * FROM users WHERE id=?"
			c = self.con.cursor()
			c.execute(sql, (userid,))

			teacher = c.fetchone()
			type = int(teacher[9])
			if type == utils.UserType.TEACHER:
				return [teacher[2] + " " + teacher[3], teacher[4]] # Return name of teacher & their E-mail
		return None

	def removeSubject(self, id):
		"""
		Removes a subject from the database if it exists.
		"""
		sql = "DELETE * FROM subjects WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()

	def addTopic(self, name, subject, description):
		"""
		Adds a topic to the database.
		"""
		sql = "INSERT INTO topics(name, subject, description) VALUES(?, ?, ?)"

		self.openConnection()

		self.con.execute(sql, (name, subject, description))

		self.con.commit()
		self.closeConnection()
	
	def removeTopic(self, id):
		"""
		Removes a topic from the database if it exists.
		"""
		sql = "DELETE * FROM topics WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()
	
	def getUserTopics(self, user):
		"""
		Returns a list of all the topics (including their tasks) set up for a user
		"""
		sql = """
		SELECT * FROM topics t
		INNER JOIN user_subjects us ON t.subject=us.subject
		WHERE us.user=?"""

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (user,))

		topics = c.fetchall()

		if len(topics) < 1:  # No topics found
			return []

		res = []
		for topic in topics:
			id = int(topic[0])
			name = topic[1]
			subject = int(topic[2])
			description = topic[3]

			# Now we have to get all tasks assigned in this topic:
			taskSql = "SELECT * FROM tasks WHERE topic=? ORDER BY date DESC"

			# Same cursor, topics have already been fetched and stored in RAM
			c.execute(taskSql, (id,))

			taskRes = c.fetchall()
			

			tasks = []
			# Check if tasks are present
			if len(taskRes) > 0:
				# Append all tasks
				for task in taskRes:
					taskData = {
						'id': int(task[0]),
						'name': task[1],
						'description': task[2],
						'date': datetime.datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S"),
						'type': int(task[4]),
						'workHours': int(task[5]),
						'subject': int(task[6]),
						'topic': int(task[7])
					}
					tasks.append(taskData)
			# Now declare dictionary with the topic variables & the topic tasks
			dic = {
				'id': id,
				'name': name,
				'subject': subject,
				'description': description,
				'tasks': tasks
			}
			res.append(dic)

		self.closeConnection()

		return res
	
	def getSubjectTopics(self, subject):
		"""
		Returns a list of all the topics (including their tasks) set up for a class subject.
		"""
		sql = "SELECT * FROM topics WHERE subject=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (subject,))

		topics = c.fetchall()

		if len(topics) < 1: # No topics found
			return []
		
		res = []
		for topic in topics:
			id = int(topic[0])
			name = topic[1]
			subject = int(topic[2])
			description = topic[3]

			# Now we have to get all tasks assigned in this topic:
			taskSql = "SELECT * FROM tasks WHERE topic=? ORDER BY date DESC"
			
			c.execute(taskSql, (id,)) # Same cursor, topics have already been fetched and stored in RAM
			
			taskRes = c.fetchall()

			tasks = []

			# Check if tasks are present
			if len(taskRes) > 0:
				# Append all tasks
				for task in taskRes:
					taskData = {
						'id': int(task[0]),
						'name': task[1],
						'description': task[2],
						'date': datetime.datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S"),
						'type': int(task[4]),
						'workHours': int(task[5]),
						'subject': int(task[6]),
						'topic': int(task[7])
					}
					tasks.append(taskData)
			# Now declare dictionary with the topic variables & the topic tasks
			dic = {
				'id': id,
				'name': name,
				'subject': subject,
				'description': description,
				'tasks': tasks
			}
			res.append(dic)

		self.closeConnection()

		return res
	
	def getSubjectData(self, id):
		"""
		Return all the data (including tasks) of a subject
		"""
		sql = "SELECT * FROM subjects WHERE id=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (id,))

		subjects = c.fetchall()

		res = []

		if len(subjects) < 1:  # No subjects
			return res

		subject = subjects[0] # Should only be one result.

		now = datetime.date.today()
		startDate = datetime.datetime.strptime(subject[5], "%Y-%m-%d").date()
		endDate = datetime.datetime.strptime(subject[6], "%Y-%m-%d").date()

		active = now <= endDate

		data = {
			'id': int(subject[0]),
			'subject': utils.Subject.name(int(subject[1])),
			'subjectid': int(subject[1]),
			'level': utils.SubjectLevel.name(int(subject[2])),
			'courseHours': int(subject[3]),
			'class': int(subject[4]),
			'startDate': startDate,
			'endDate': endDate,
			'active': active
		}
		res.append(data)

		topics = self.getSubjectTopics(int(subject[0]))

		data['topics'] = topics

		return data

	def addClass(self, name, year, lineOfStudy):
		"""
		Adds a class to the database and returns the id of the new class.
		"""
		sql = "INSERT INTO classes(name, year, line_of_study) VALUES(?, ?, ?)"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (name, year, lineOfStudy))

		classid = c.lastrowid

		self.con.commit()
		self.closeConnection()

		return classid
	
	def removeClass(self, id):
		"""
		Removes a class from the database if it exists.
		"""
		sql = "DELETE * FROM classes WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()
	
	def getClass(self, id):
		"""
		Returns a dictionary with information about a class.
		"""
		sql = "SELECT * FROM classes WHERE id=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (id,))

		res = c.fetchall()

		self.closeConnection()

		if len(res) < 1: # No class found
			return None
		
		clazz = res[0]

		return {
			'id': int(clazz[0]),
			'name': clazz[1],
			'year': int(clazz[2]),
			'study': int(clazz[3])
		}

	def getClasses(self):
		"""
		Returns a list of dictionaries with all classes
		"""
		sql = "SELECT * FROM classes"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql)

		classes = c.fetchall()

		self.closeConnection()

		if len(classes) < 1: # No classes found
			return []
		
		res = []
		for clazz in classes: # 'class' is a protected word
			dic = {
				'id': int(clazz[0]),
				'name': clazz[1],
				'year': int(clazz[2]),
				'study': int(clazz[3])
			}
			res.append(dic)
		
		return res
	
	def editClass(self, id, name, year, study):
		"""
		Updates a class in the database with edited values
		"""
		sql = "UPDATE classes SET name=?,year=?,line_of_study=? WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (name, year, study, id))

		self.con.commit()
		self.closeConnection()
	
	def getClassStudents(self, clazz):
		"""
		Returns a list of all the id's of students in a class
		"""
		sql = "SELECT * FROM users WHERE class=?"

		self.openConnection()

		c = self.con.cursor()
		c.execute(sql, (clazz,))

		students = c.fetchall()

		self.closeConnection()

		if len(students) < 1: # No students found
			return []
		
		res = []
		for student in students:
			studentid = int(student[0])
			res.append(studentid)
		return res

	def editUserClass(self, user, clazz):
		"""
		Changes the user's class to the given class id. Should rarely be used.
		"""
		sql = "UPDATE users SET class=? WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (clazz, user))

		self.con.commit()
		self.closeConnection()

	def addExam(self, subject, level, date):
		"""
		Adds an exam to given subject with given level to the database.
		"""
		sql = "INSERT INTO exams(subject, level, date) VALUES(?, ?, ?)"
		
		self.openConnection()
		
		self.con.execute(sql, (subject, level, date))

		self.con.commit()
		self.closeConnection()
	
	def removeExam(self, id):
		"""
		Removes an exam from the database if it exists.
		"""
		sql = "DELETE * FROM exams WHERE id=?"

		self.openConnection()

		self.con.execute(sql, (id,))

		self.con.commit()
		self.closeConnection()

# Following is used for testing
if __name__ == "__main__":
	data = Data()

	data.getUserLateAssignments(1)
