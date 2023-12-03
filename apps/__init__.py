import os

from dotenv import dotenv_values
from flask import Flask, url_for

from apps.hello import hello_bp


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(dotenv_values())

    # register blueprints
    app.register_blueprint(hello_bp)

    @app.route('/')
    def default():
        return f"Checkout route <a href={url_for('hello_bp.default')}>hello<a/>"

    return app
