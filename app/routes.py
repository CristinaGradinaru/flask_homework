from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def hello_world():
    title = 'Top 5 | HOME'
    return render_template('index.html', title= title)

@app.route('/favorite5')
def favorite5():
    context = {
        'title': 'Top 5 Comedians | FAVORITE5',
        'comedians':{
            1: 'Dave Chappelle',
            2: 'Patrice O\'Neal',
            3: 'Whitney Cummings',
            4: 'Chris Rock',
            5: 'Bill Burr'
        }
    }
    return render_template("favorite5.html", **context)