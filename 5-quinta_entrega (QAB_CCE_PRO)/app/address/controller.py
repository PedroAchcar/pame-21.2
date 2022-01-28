from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.extensions import db
from .models import Address


class Endereco(MethodView):  # /endereco/<int:endereco_id>
    decorators = [jwt_required()]

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

            if not isinstance(cep, str) or not isinstance(logradouro, str) \
                    or not isinstance(numero, int) or not isinstance(bairro, str) \
                    or not isinstance(cidade, str) or not isinstance(estado, str):
                return {'error': 'invalid data'}, 400

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


class Enderecos(MethodView):  # /enderecos
    decorators = [jwt_required()]

    def get(self):
        enderecos = Address.query.all()

        return jsonify([endereco.json() for endereco in enderecos]), 200

    def post(self):
        body = request.json

        try:
            cep = body.get('cep')
            logradouro = body.get('logradouro')
            numero = body.get('numero')
            bairro = body.get('bairro')
            cidade = body.get('cidade')
            estado = body.get('estado')

            if not isinstance(cep, str) or not isinstance(logradouro, str) \
                    or not isinstance(numero, int) or not isinstance(bairro, str) \
                    or not isinstance(cidade, str) or not isinstance(estado, str):
                return {'error': 'invalid data'}, 400

            if cep == None:
                return {'error': 'faltando dados'}, 400

            endereco = Address(cep=cep,
                               logradouro=logradouro,
                               numero=numero,
                               bairro=bairro,
                               cidade=cidade,
                               estado=estado)

            db.session.add(endereco)
            db.session.commit()

            return endereco.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400
