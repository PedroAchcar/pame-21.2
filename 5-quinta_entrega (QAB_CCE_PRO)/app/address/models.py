from app.extensions import db


class Address(db.Model):
    __tablename__ = 'endereco'

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), nullable=False)
    logradouro = db.Column(db.String)
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)

    user = db.relationship("User", backref="endereco")

    def json(self):
        return {
            'id': self.id,
            'CEP': self.cep,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
        }
