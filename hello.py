from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

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
    return render_template('comments.html', comments = comments)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500