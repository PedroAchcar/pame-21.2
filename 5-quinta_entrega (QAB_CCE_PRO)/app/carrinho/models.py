from app.extensions import db


class Carrinho(db.Model):
    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True)
    data_compra = db.Column(db.DateTime, server_default=db.func.now())
    valor_total = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item = db.relationship("Item", backref="carrinho")

    def json(self):
        return {
            'id': self.id,
            'valor_total': self.valor_total,
            'data_compra': self.data_compra,
            'user_id': self.user_id,
            'itens': self.item
        }
