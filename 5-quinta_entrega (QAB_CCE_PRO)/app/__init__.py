from flask import Flask

from .config import Config
from .extensions import db, migrate, mail, jwt

from app.user.routes import user_api
from app.address.routes import endereco_api
from app.produto.routes import product_api
from app.carrinho.routes import carrinho_api
from app.item.routes import item_api


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(endereco_api)
    app.register_blueprint(product_api)
    app.register_blueprint(carrinho_api)
    app.register_blueprint(item_api)

    return app
