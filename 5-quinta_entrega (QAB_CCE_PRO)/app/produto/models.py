from app.extensions import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(150))
    valor = db.Column(db.Float, nullable=False)

    item = db.relationship("Item", backref="product", uselist=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': round(self.valor, 2)
        }
