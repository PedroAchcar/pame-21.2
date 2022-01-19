from app.extensions import db
from flask import Blueprint

user_api = Blueprint('user_api', __name__)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(15))
    email = db.Column(db.String(50), unique=True, index=True)
    address = db.Column(db.String(50))
    cpf = db.Column(db.String(15), unique=True)

    cupom = db.relationship('Cupom', backref='user')
    carrinho = db.relationship('Carrinho', backref='user', uselist=False)

    def json(self):
        return {
            'Nome': self.nome,
            'Telefone': self.phone
        }
