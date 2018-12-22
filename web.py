#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<html></head><title>Test Page</title></head><body><h1>Welcome!</h1></body</html>"











if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=80)
