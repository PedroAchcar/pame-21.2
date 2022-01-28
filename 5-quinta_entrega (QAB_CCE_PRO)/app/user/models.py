from app.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String(15))
    cpf = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True, index=True)
    senha_hash = db.Column(db.String(200), nullable=False)

    endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id"))
    carrinho = db.relationship("Carrinho", backref="user", uselist=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'CPF': self.cpf,
            'telefone': self.telefone,
            'e-mail': self.email,
            'endereco_id': self.endereco_id,
            'carrinho_id': self.carrinho
        }
