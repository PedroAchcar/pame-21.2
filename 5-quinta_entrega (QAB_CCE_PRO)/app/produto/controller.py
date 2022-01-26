from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
from app.produto.models import Product


class Produtos(MethodView):  # /produtos
    def get(self):
        produtos = Product.query.all()

        return jsonify([prod.json() for prod in produtos]), 200

    def post(self):
        body = request.json

        try:
            nome = body.get('nome')
            descricao = body.get('descricao')
            valor = body.get('valor')

            if nome == None or valor == None:
                return {'error': 'faltando dados'}, 400

            user = Product(nome=nome, descricao=descricao, valor=valor)

            db.session.add(user)
            db.session.commit()

            return user.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400


class ProdutoById(MethodView):  # /produto/<int:produto_id>
    def get(self, produto_id):
        prod = Product.query.get_or_404(produto_id)

        return prod.json(), 200

    def put(self, produto_id):
        prod = Product.query.get_or_404(produto_id)
        body = request.json

        try:
            nome = body.get('nome')
            descricao = body.get('descricao')
            valor = body.get('valor')

            if nome == None or descricao == None or valor == None:
                return {'error': 'faltando dados'}, 400

            prod.nome = nome
            prod.descricao = descricao
            prod.valor = valor

            db.session.commit()

            return prod.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400

    def patch(self, produto_id):
        prod = Product.query.get_or_404(produto_id)
        body = request.json

        try:
            nome = body.get('nome', prod.nome)
            descricao = body.get('descricao', prod.descricao)
            valor = body.get('valor', prod.valor)

            prod.nome = nome
            prod.descricao = descricao
            prod.valor = valor

            db.session.commit()

            return prod.json(), 200

        except:
            return {'error': 'ocorreu um erro'}, 400

    def delete(self, produto_id):
        prod = Product.query.get_or_404(produto_id)

        db.session.delete(prod)
        db.session.commit()

        return prod.json(), 200
