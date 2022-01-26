from app.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, index=True)
    cpf = db.Column(db.String(15), unique=True)

    endereco = db.relationship("Endereco", backref="user")
    carrinho = db.relationship("Carrinho", backref="user", uselist=False)

    def json(self):
        return {
            'nome': self.nome,
            'CPF': self.cpf,
            'telefone': self.telefone,
            'e-mail': self.email,
        }


class Address(db.Model):
    __tablename__ = 'endereco'

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), nullable=False)
    logradouro = db.Column(db.String)
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def json(self):
        return {
            'CEP': self.cep,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
        }
