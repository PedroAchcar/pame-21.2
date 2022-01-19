from datetime import datetime
from app.extensions import db
from flask import Blueprint

carrinho_api = Blueprint('carrinho_api', __name__)


class Carrinho(db.Model):
    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True)
    data_compra = db.Column(db.DateTime, default=datetime.now)
    valor_total = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item = db.relationship('Item', backref='carrinho')

    def json(self):
        return {
            'Valor Total': self.valor_total,
            'Data da Compra': self.data_compra
        }


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    carro = db.Column(db.Boolean)
    moto = db.Column(db.Boolean)
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)

    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

    def json(self):
        return {
            'id': self.id,
            'Quantidade': self.quantidade,
            'Valor': self.valor
        }
