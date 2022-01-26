from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
from app.user.models import User, Address


class Endereco(MethodView):  # /endereco/<int:endereco_id>
    def get(self, endereco_id):
        endereco = Address.query.filter_by(id=endereco_id).first()

        return endereco.json(), 200

    def patch(self, endereco_id):
        endereco = Address.query.get_or_404(endereco_id)
        body = request.json

        try:
            cep = body.get('cep', endereco.cep)
            logradouro = body.get('logradouro', endereco.logradouro)
            numero = body.get('numero', endereco.numero)
            bairro = body.get('bairro', endereco.bairro)
            cidade = body.get('cpf', endereco.cidade)
            estado = body.get('cpf', endereco.estado)

            endereco.cep = cep
            endereco.logradouro = logradouro
            endereco.numero = numero
            endereco.bairro = bairro
            endereco.cpf = cidade
            endereco.cpf = estado

            db.session.commit()

            return endereco.json(), 200

        except:
            return {'error': 'ocorreu um erro'}, 400

    def delete(self, endereco_id):
        endereco = Address.query.get_or_404(endereco_id)

        db.session.delete(endereco)
        db.session.commit()

        return endereco.json(), 200


class Enderecos(MethodView):  # /enderecos/<int:user_id>
    def get(self, user_id):
        enderecos = Address.query.filter_by(user_id=user_id)

        return jsonify([endereco.json() for endereco in enderecos]), 200

    def post(self, user_id):
        body = request.json

        try:
            cep = body.get('cep')
            logradouro = body.get('logradouro')
            numero = body.get('numero')
            bairro = body.get('bairro')
            cidade = body.get('cidade')
            estado = body.get('estado')

            if cep == None:
                return {'error': 'faltando dados'}, 400

            endereco = Address(cep=cep,
                               logradouro=logradouro,
                               numero=numero,
                               bairro=bairro,
                               cidade=cidade,
                               estado=estado,
                               user_id=user_id)

            db.session.add(endereco)
            db.session.commit()

            return endereco.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400


class Usuarios(MethodView):  # /usuarios
    def get(self):
        users = User.query.all()

        return jsonify([usuario.json() for usuario in users]), 200

    def post(self):
        body = request.json

        try:
            nome = body.get('nome')
            telefone = body.get('telefone')
            email = body.get('email')
            cpf = body.get('cpf')

            if nome == None or telefone == None:
                return {'error': 'faltando dados'}, 400

            user = User(nome=nome, telefone=telefone, email=email, cpf=cpf)

            db.session.add(user)
            db.session.commit()

            return user.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400


class Usuario(MethodView):  # /usuario/<int:id>
    def get(self, id):
        user = User.query.get_or_404(id)

        return user.json(), 200

    def put(self, id):
        user = User.query.get_or_404(id)
        body = request.json

        try:
            nome = body.get('nome')
            telefone = body.get('telefone')
            email = body.get('email')
            cpf = body.get('cpf')

            if nome == None or telefone == None or email == None or cpf == None:
                return {'error': 'faltando dados'}, 400

            user.nome = nome
            user.telefone = telefone
            user.email = email
            user.cpf = cpf

            db.session.commit()

            return user.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400

    def patch(self, id):
        user = User.query.get_or_404(id)
        body = request.json

        try:
            nome = body.get('nome', user.nome)
            telefone = body.get('telefone', user.telefone)
            email = body.get('email', user.email)
            cpf = body.get('cpf', user.cpf)

            user.nome = nome
            user.telefone = telefone
            user.email = email
            user.cpf = cpf

            db.session.commit()

            return user.json(), 200

        except:
            return {'error': 'ocorreu um erro'}, 400

    def delete(self, id):
        user = User.query.get_or_404(id)

        db.session.delete(user)
        db.session.commit()

        return user.json(), 200
