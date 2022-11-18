from flask import Flask,render_template

def create_app():
    app = Flask(__name__)
  return app

@app.route("/")
def hello_world():
  return render_template('base.html')
