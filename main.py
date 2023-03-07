from flask import Flask

app = Flask(__name__)

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

if __name__ == "__main__":
	app.run(debug=True)
