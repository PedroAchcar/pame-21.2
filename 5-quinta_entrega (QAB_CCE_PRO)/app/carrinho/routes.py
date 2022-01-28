from flask import Blueprint
from .controller import CartById


carrinho_api = Blueprint('carrinho_api', __name__)


carrinho_api.add_url_rule('/carrinho/<int:user_id>',
                          view_func=CartById.as_view('carrinho'),
                          methods=['GET', 'POST', 'DELETE'])
