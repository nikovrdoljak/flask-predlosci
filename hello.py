from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.route('/user/')
def nouser():
    return render_template('user.html')

@app.route('/comments/')
def comments():
    comments = ['Odlično!', 'HŽV', 'Ništa ne razumijem', 'Nije loše za prvi put...']
    return render_template('user.html', comments = comments)

