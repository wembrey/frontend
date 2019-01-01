from frontend import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    demo = {'demo': 'Sec Ops'}
    return "Hello, World!"
    return render_template('index.html', title='Home', demo=demo)
