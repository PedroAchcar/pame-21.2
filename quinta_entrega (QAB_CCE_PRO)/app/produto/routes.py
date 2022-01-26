from flask import Blueprint
from .controller import Produtos, ProdutoById


product_api = Blueprint('product_api', __name__)


product_api.add_url_rule('/produtos',
                         view_func=Produtos.as_view('produtos'),
                         methods=['GET', 'POST'])

product_api.add_url_rule('/produto/<int:produto_id>',
                         view_func=ProdutoById.as_view('produto_by_id'),
                         methods=['GET', 'PUT', 'PATCH', 'DELETE'])
