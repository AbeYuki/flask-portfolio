from flask import Flask, Blueprint, render_template, redirect, url_for, request

def create_app():
    app = Flask(__name__, static_folder='./static/images', static_url_path='/portfolio/static/images')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
