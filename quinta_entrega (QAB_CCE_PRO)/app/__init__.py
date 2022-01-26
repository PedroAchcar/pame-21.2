from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.user.models import user_api


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(user_api)

    return app
