#!/usr/bin/env python

from flask import flask

app = flask(__name__)

@app.route("/")
def main():
    return "<html></head><title>Test Page</title></head><body><h1>Welcome!</h1></body</html>"











if __name__=="__main__":
    app.run()
