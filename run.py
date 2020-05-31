import os
from flask import Flask

# initiliasing flask application
app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def username(username):
    return "Hi " + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)

# we use os.getenv('IP') to get the IP address
app.run(host=os.getenv('IP'), port= (os.getenv('PORT')), debug= True)