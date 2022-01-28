from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.extensions import db
from app.carrinho.models import Carrinho


class CartById(MethodView):  # /carrinho/<int:user_id>
    decorators = [jwt_required()]

    def get(self, user_id):
        try:
            cart = Carrinho.query.filter_by(user_id=user_id).first()
            return cart.json(), 200

        except Exception:
            return {'error': 'carrinho nao pertence a nenhum usuario'}, 400

    def post(self, user_id):

        item = Carrinho(user_id=user_id)

        db.session.add(item)
        db.session.commit()

        return item.json(), 200

    def delete(self, user_id):
        try:
            cart = Carrinho.query.filter_by(user_id=user_id).first()

            db.session.delete(cart)
            db.session.commit()

            return {'user_id': user_id,
                    'status': 'apagado com sucesso',
                    }, 200

        except Exception:
            return {'error': 'carrinho nao pertence a nenhum usuario'}, 400
