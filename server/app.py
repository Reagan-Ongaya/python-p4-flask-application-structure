#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#Defining a route by the use of @app.route decorator
@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

#parameterizing  a part in our route 
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555)