from flask import Flask, Blueprint, render_template, redirect, url_for, request,jsonify, abort
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import inspect

db = SQLAlchemy()
migrate = Migrate() 

def create_app():
    app = Flask(__name__, static_folder='./static/images', static_url_path='/portfolio/static/images')
    app.config.from_object('portfolio.config.Config')
    
    from .models.users import Users 
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        inspector = inspect(db.engine)
        if inspector.has_table('users'):
            create_init_user(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def create_init_user(app):
    with app.app_context():
        from .models.users import Users
        from .init.data.users import admin_user_data
        from .models.users import Users
        admin_user = Users.query.filter_by(user_email="admin@example.com").first()
        if not admin_user:
            admin_user = Users(
                user_name=admin_user_data["user_name"],
                user_email=admin_user_data["user_email"],
                user_pass=admin_user_data["user_pass"]
            )
            db.session.add(admin_user)
            try:
                db.session.commit()
            except Exception as e:
                print(f"Error adding admin user: {e}")
