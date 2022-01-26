from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
from app.carrinho.models import Carrinho, Item


class CartById(MethodView):  # /carrinho/<int:user_id>
    def get(self, user_id):
        try:
            cart = Carrinho.query.filter_by(user_id=user_id).first()
            return cart.json(), 200

        except Exception:
            return {'error': 'carrinho nao pertence a nenhum usuario'}, 400

    def delete(self, user_id):
        try:
            cart = Carrinho.query.filter_by(user_id=user_id).first()

            db.session.delete(cart)
            db.session.commit()

            return cart.json(), 200

        except Exception:
            return {'error': 'carrinho nao pertence a nenhum usuario'}, 400


class Itens(MethodView):  # /itens
    def get(self):
        itens = Item.query.all()

        return jsonify([item.json() for item in itens]), 200

    def post(self):
        body = request.json

        try:
            quantidade = body.get('quantidade')
            carrinho_id = body.get('carrinho_id')
            produto_id = body.get('produto_id')

            if quantidade == None or carrinho_id == None or produto_id == None:
                return {'error': 'faltando dados'}, 400

            item = Item(quantidade=quantidade,
                        carrinho_id=carrinho_id,
                        produto_id=produto_id)

            db.session.add(item)
            db.session.commit()

            return item.json(), 200

        except Exception as e:
            print(e)
            return {'error': 'algum erro ocorreu'}, 400


class ItemById(MethodView):  # /itens/<item_id>
    def get(self, item_id):
        try:
            item = Item.query.filter_by(item_id=item_id).first()
            return item.json(), 200

        except Exception:
            return {'error': 'item nao existe'}, 400

    def patch(self, item_id):
        item = Item.query.get_or_404(item_id)
        body = request.json

        try:
            # A ideia eh somente alterar a quantidade, não podendo alterar o carrinho
            # nem o produto (somente apagando esse item do carrinho)
            quantidade = body.get('quantidade', item.quantidade)
            carrinho_id = item.carrinho_id
            produto_id = item.produto_id

            item.quantidade = quantidade
            item.carrinho_id = carrinho_id
            item.produto_id = produto_id

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

        except Exception:
            return {'error': 'item nao existe'}, 400
