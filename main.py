from flask import Flask

app = Flask(__name__)

# A dictionary stores all user's habits
# @key : user name
# @value : A list of habit object
UsersHabits = {}

@app.route("/")
def test():
	return "Hello World!"

@app.route("/register", methods=['POST'])
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

if __name__ == "__main__":
	# read user's habits frmo disk here
	app.run(debug=True)
