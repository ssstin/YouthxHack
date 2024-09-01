# webpage.py
from flask import Flask
from src import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main.bp)
    return app