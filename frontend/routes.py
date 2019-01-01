from frontend import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    demo = {'type': 'Sec Ops'}
    return render_template('index.html', title='Home', demo=demo)
