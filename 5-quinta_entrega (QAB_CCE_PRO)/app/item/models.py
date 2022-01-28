from app.extensions import db


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)

    carrinho_id = db.Column(db.Integer, db.ForeignKey("carrinho.id"))
    produto_id = db.Column(db.Integer, db.ForeignKey("product.id"))

    def json(self):
        return {
            'id': self.id,
            'quantidade': self.quantidade,
            'carrinho_id': self.carrinho_id,
            'produto_id': self.produto_id
        }
