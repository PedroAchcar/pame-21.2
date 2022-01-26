from app.extensions import db


class Product(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150))
    valor = db.Column(db.Float, nullable=False)

    # item = db.relationship("Item", backref="produto", uselist=False)
    # NÃO TENHO CERTEZA DESSA RELAÇÃO /\, UM PRODUTO NÃO TEM ITEM PORÉM ITEM TEM PRODUTO SEMPRE.

    def json(self):
        return {
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': round(self.valor, 2)
        }
