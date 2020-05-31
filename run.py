import os
from flask import Flask

# initiliasing flask application
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello There!</h1>"

# we use os.getenv('IP') to get the IP address
app.run(host=os.getenv('IP'), port= (os.getenv('PORT')), debug= True)