from flask import Blueprint
from .controller import Usuario, Usuarios, Endereco, Enderecos


user_api = Blueprint('user_api', __name__)


user_api.add_url_rule('/endereco/<int:endereco_id>',
                      view_func=Endereco.as_view('endereco'),
                      methods=['GET', 'PATCH', 'DELETE'])

user_api.add_url_rule('/enderecos/<int:user_id>',
                      view_func=Enderecos.as_view('enderecos'),
                      methods=['GET', 'POST'])

user_api.add_url_rule('/usuarios',
                      view_func=Usuario.as_view('usuario'),
                      methods=['GET', 'POST'])

user_api.add_url_rule('/usuario/<int:user_id>',
                      view_func=Usuarios.as_view('usuarios'),
                      methods=['GET', 'PUT', 'PATCH', 'DELETE'])
