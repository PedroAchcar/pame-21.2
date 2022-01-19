from flask import Flask
from .config import Config
from .extensions import db, migrate
from user.models import user_api
from carro.models import carro_api
from moto.models import moto_api
from carrinho.models import carrinho_api


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(carro_api)
    app.register_blueprint(moto_api)
    app.register_blueprint(carrinho_api)

    migrate.init_app(app, db)

    return app
