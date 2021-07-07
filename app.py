#!/usr/bin/env python3 

from flask import Flask

app = Flask(__name__)

# welcome
@app.route("/welcome")
def welcome():
	"""Routes to welcome page"""

	html = f"""
		<!DOCTYPE html>
		<html lang="en">
		<body>
			<h1>Welcome!</h1>
		</body>
		</html>
	"""

	return html
# welcome home

@app.route("/welcome/<endpoint>")
def welcome_home(endpoint):
	"""Routes to any endpoint"""
	return f"""
		<!DOCTYPE html>
		<html lang="en">

		<body>
			<h1>Welcome {endpoint}!</h1>
		</body>
		</html>
	"""
# welcome back
