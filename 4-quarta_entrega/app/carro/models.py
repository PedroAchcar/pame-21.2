from app.extensions import db
from flask import Blueprint

carro_api = Blueprint('carro_api', __name__)


class Carro(db.Model):
    __tablename__ = 'carro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False, index=True)
    ano = db.Column(db.Integer)
    combustivel = db.Column(db.String(15))
    valor = db.Column(db.Float, nullable=False)

    def json(self):
        return {
            'Carro': self.nome,
            'Marca': self.marca,
            'Valor': round(self.valor, 2)
        }
