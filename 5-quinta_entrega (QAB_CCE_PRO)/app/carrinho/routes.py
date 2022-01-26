from flask import Blueprint
from .controller import CartById, Itens, ItemById


carrinho_api = Blueprint('carrinho_api', __name__)


carrinho_api.add_url_rule('/carrinho/<int:user_id>',
                          view_func=CartById.as_view('carrinho'),
                          methods=['GET', 'DELETE'])

carrinho_api.add_url_rule('/itens',
                          view_func=Itens.as_view('itens'),
                          methods=['GET', 'POST'])

carrinho_api.add_url_rule('/itens/<item_id>',
                          view_func=ItemById.as_view('item_by_id'),
                          methods=['GET', 'PATCH', 'DELETE'])
