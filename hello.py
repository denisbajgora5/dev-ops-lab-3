from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # HTML link to the /about page
    return '<p>Hello, World!</p><a href="/about">About</a>'

@app.route('/about')
def about():
    # Simple about page content
    return '<p>This is a Flask web app running in a Linux VM.</p>'
