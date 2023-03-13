from flask import Flask, jsonify, request
from Habit import Habit
from MySQL import MySQL
app = Flask(__name__)
sql = MySQL()
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

# url : "/newuser?username=USERNAME"
@app.route("/newuser", methods=['POST'])
def RegisterUser():
	username = request.args.get('username', default = "", type = str)
	print(username)
	sql.createUser(username)
	return ('', 204)

# url : "/habit?username=USERNAME"
@app.route("/habit", methods = ['GET'])
def GetHabit():
	username = request.args.get('username', default = "", type = str)
	raw_data = sql.readHabit(username)
	data_json = []
	for data in raw_data:
		now = Habit(data[0])
		data_json.append(now.toDict())
	return jsonify(data_json)

@app.route("/habit", methods = ['POST'])
def AddNewHabit():
	username = request.args.get('username', default = "", type = str)
	newhabit = request.json
	sql.insertHabit(username, Habit(newhabit['HabitName']))
	return ('', 204)

@app.route("/habit", methods = ['DELETE'])
def DeleteHabit():
	username = request.args.get('username', default = "", type = str)
	habit = request.json
	sql.deleteHabit(username, habit['HabitName'])
	return ('', 204)

if __name__ == "__main__":
	# read user's habits from disk here
	app.run(debug=True, host = '0.0.0.0')
