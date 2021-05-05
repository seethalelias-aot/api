import flask
from flask import jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
books = [
	{
	'id' = 1,
	'title' = 'once upon a time',
	'year' = 2000
	},
	{
	'id' = 2,
	'title' = 'stars'
	'year' = 1998
	}
]
@app.route('/', methods = ['GET'])
def home():
	return "<h1> books </h1>"
	return jsonify(books)
app.run()