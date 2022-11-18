from flask import Flask, Blueprint, render_template, redirect, url_for, request

def create_app():
    app = Flask(__name__)
    return app

app = Blueprint('app', __name__)

@app.route("/")
def hello_world():
  return render_template('base.html')
