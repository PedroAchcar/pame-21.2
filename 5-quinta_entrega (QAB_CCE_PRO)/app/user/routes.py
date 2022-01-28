from flask import Blueprint
from .controller import Usuario, Usuarios, UsuarioLogin


user_api = Blueprint('user_api', __name__)


user_api.add_url_rule('/usuarios',
                      view_func=Usuarios.as_view('usuarios'),
                      methods=['GET', 'POST'])

user_api.add_url_rule('/usuario/<int:id>',
                      view_func=Usuario.as_view('usuario'),
                      methods=['GET', 'PUT', 'PATCH', 'DELETE'])

user_api.add_url_rule('/login',
                      view_func=UsuarioLogin.as_view('login'),
                      methods=['POST'])
