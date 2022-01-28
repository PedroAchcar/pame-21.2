from flask import Blueprint
from .controller import Endereco, Enderecos


endereco_api = Blueprint('endereco_api', __name__)


endereco_api.add_url_rule('/endereco/<int:endereco_id>',
                          view_func=Endereco.as_view('endereco'),
                          methods=['GET', 'PATCH', 'DELETE'])

endereco_api.add_url_rule('/enderecos',
                          view_func=Enderecos.as_view('enderecos'),
                          methods=['GET', 'POST'])
