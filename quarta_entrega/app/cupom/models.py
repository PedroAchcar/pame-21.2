from app.extensions import db


class Cupom(db.Model):
    __tablename__ = 'cupom'

    id = db.Column(db.Integer, primary_key=True)
    porcentagem = db.Column(db.Integer, nullable=False, default=10)
    carro = db.Column(db.Boolean, default=True)
    moto = db.Column(db.Boolean, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def json(self):
        return {
            'Porcentagem': self.porcentagem,
            'Carro': self.carro,
            'Moto': self.moto
        }
