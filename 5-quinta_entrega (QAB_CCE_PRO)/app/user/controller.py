import bcrypt

from flask import jsonify, render_template, request
from flask.views import MethodView
from flask_mail import Message
from flask_jwt_extended import create_access_token, jwt_required

from app.sensive import Sensive as sv
from app.extensions import db, mail
from app.user.models import User
from app.address.models import Address


class Usuarios(MethodView):  # /usuarios
    decorators = [jwt_required()]

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
            senha = body.get('senha')

            if not isinstance(nome, str) or not isinstance(telefone, str) \
                    or not isinstance(email, str) or not isinstance(cpf, str) \
                    or not isinstance(senha, str):
                return {'error': 'invalid data'}, 400

            if nome == None or email == None or senha == None:
                return {'error': 'faltando dados'}, 400

            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

            user = User(nome=nome,
                        telefone=telefone,
                        email=email,
                        senha_hash=senha_hash,
                        cpf=cpf)

            db.session.add(user)
            db.session.commit()

            msg = Message(
                sender=sv.MAIL_SENDER,
                recipients=[email],
                subject='Bem-Vindo!',
                html=render_template('email.html', nome=nome)
            )

            mail.send(msg)

            return user.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400


class Usuario(MethodView):  # /usuario/<int:id>
    decorators = [jwt_required()]

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

            if not isinstance(nome, str) or not isinstance(telefone, str) \
                    or not isinstance(email, str) or not isinstance(cpf, str):
                return {'error': 'invalid data'}, 400

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
            endereco = Address.query.get_or_404(body.get('endereco'))

            if not isinstance(nome, str) or not isinstance(telefone, str) \
                    or not isinstance(email, str) or not isinstance(cpf, str) \
                    or not isinstance(endereco, str):
                return {'error': 'invalid data'}, 400

            user.nome = nome
            user.telefone = telefone
            user.email = email
            user.cpf = cpf
            user.endereco = endereco

            db.session.commit()

            return user.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'ocorreu um erro'}, 400

    def delete(self, id):
        user = User.query.get_or_404(id)

        db.session.delete(user)
        db.session.commit()

        return {'user_id': id,
                'status': 'apagado com sucesso',
                }, 200


class UsuarioLogin(MethodView):  # /login
    def post(self):
        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        if not isinstance(email, str) or not isinstance(senha, str):
            return {'error': 'invalid data'}, 400

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.checkpw(senha.encode(), user.senha_hash):
            return {'error': 'email ou senha incorretos'}, 400

        token = create_access_token(identity=user.id)

        return {"user": user.json(),
                'token': token}, 200
