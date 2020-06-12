from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title="The page you were looking for does not exist (404)"), 404
