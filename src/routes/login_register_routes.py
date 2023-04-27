from flask import Blueprint
from controllers.login_register_controller import(
    register,
    login
)
login_bp = Blueprint('auth', __name__, url_prefix='/auth')

login_bp.route('/', methods=['POST'])(register)
login_bp.route('/login', methods=['POST'])(login)

