from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/portfolio/')
def index():
    return render_template('index.html')

@main.route('/portfolio/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')

@main.route('/portfolio/software')
def software():
    return render_template('software.html')

@main.route('/portfolio/ci-cd')
def ci_cd():
    return render_template('ci-cd.html')