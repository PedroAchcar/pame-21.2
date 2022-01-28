from flask import Blueprint
from .controller import Itens, ItemById


item_api = Blueprint('item_api', __name__)


item_api.add_url_rule('/itens/<int:cart_id>',
                      view_func=Itens.as_view('itens'),
                      methods=['GET', 'POST'])

item_api.add_url_rule('/item/<item_id>',
                      view_func=ItemById.as_view('item_by_id'),
                      methods=['GET', 'PATCH', 'DELETE'])
