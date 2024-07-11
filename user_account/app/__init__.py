from flask import Flask
from app.views import user_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")
    app.register_blueprint(user_bp)
    return app