from flask import Flask
from flask import jsonify
from Habit import Habit

app = Flask(__name__)

# A dictionary stores all user's habits
# @key : user name
# @value : A list of habit object
UsersHabits = {}

@app.route("/")
def test():
	tmp = []
	for i in range(5):
		now = Habit("HASH" + str(i))
		tmp.append(now.toDict())
	return jsonify(tmp)

@app.route("/newuser", methods=['POST'])
def RegisterUser():
	raise NotImplementedError

@app.route("/habit", methods = ['GET'])
def Gethabit():
	raise NotImplementedError

@app.route("/habit", methods = ['POST'])
def AddNewHabit():
	raise NotImplementedError

@app.route("/habit", methods = ['DELETE'])
def DeleteHabit():
	raise NotImplementedError



# Read user's file from sql 
# @username : user's name
# @return : List of Habit which are user's habits
def ReadSQL(username):
	raise NotImplementedError


# Read user's file from sql 
# @username : user's name
# @newHabit : habit to be inserted
# @return : List of Habit which are user's habits
def InsertSQL(username, newHabit):
	raise NotImplementedError


# Read user's file from sql 
# @username : user's name
# @eraseHabit : habit to be deleted
# @return : List of Habit which are user's habits
def DeleteSQL(username, eraseHabit):
	raise NotImplementedError


if __name__ == "__main__":
	# read user's habits from disk here
	app.run(debug=True)
