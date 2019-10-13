from flask import  Flask
app = Flask(__name__)

@app.route("/okay")
def hello():
	a= 2+2
	return {"value": a}