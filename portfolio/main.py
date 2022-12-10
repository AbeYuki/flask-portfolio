from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')