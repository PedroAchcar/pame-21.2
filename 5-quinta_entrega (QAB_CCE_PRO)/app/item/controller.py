from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.extensions import db
from .models import Item


class Itens(MethodView):  # /itens/<int:cart_id>
    decorators = [jwt_required()]

    def get(self, cart_id):
        itens = Item.query.filter_by(carrinho_id=cart_id)

        return jsonify([item.json() for item in itens]), 200

    def post(self, cart_id):
        body = request.json

        try:
            quantidade = body.get('quantidade')
            produto_id = body.get('produto_id')

            if not isinstance(quantidade, int) or not isinstance(produto_id, int):
                return {'error': 'invalid data'}, 400

            if quantidade == None or produto_id == None:
                return {'error': 'faltando dados'}, 400

            item = Item(quantidade=quantidade,
                        carrinho_id=cart_id,
                        produto_id=produto_id)

            db.session.add(item)
            db.session.commit()

            return item.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400


class ItemById(MethodView):  # /item/<item_id>
    def get(self, item_id):
        try:
            item = Item.query.filter_by(id=item_id).first()
            return item.json(), 200

        except Exception:
            return {'error': 'item nao existe'}, 400

    def patch(self, item_id):
        item = Item.query.get_or_404(item_id)
        body = request.json

        try:
            # A ideia eh somente alterar a quantidade, não podendo alterar o carrinho
            # nem o produto correspondente (somente apagando esse item do carrinho)
            quantidade = body.get('quantidade', item.quantidade)

            if not isinstance(quantidade, int):
                return {'error': 'invalid data'}, 400

            item.quantidade = quantidade
            item.carrinho_id = item.carrinho_id
            item.produto_id = item.produto_id

            db.session.commit()

            return item.json(), 200

        except:
            return {'error': 'ocorreu um erro'}, 400

    def delete(self, item_id):
        try:
            item = Item.query.filter_by(item_id=item_id).first()

            db.session.delete(item)
            db.session.commit()

            return item.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400
