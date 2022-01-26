from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.user.routes import user_api
from app.produto.routes import product_api
from app.carrinho.routes import carrinho_api


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(user_api)
    app.register_blueprint(product_api)
    app.register_blueprint(carrinho_api)

    return app
