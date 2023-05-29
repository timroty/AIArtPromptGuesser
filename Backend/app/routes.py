from flask import Blueprint, jsonify, current_app
from .supabase import Supabase
# from app.handlers import get_all_users, get_user, create_user

bp = Blueprint('api', __name__)
spc = Supabase()

@bp.route('/image', methods=['GET'])
def users():
    return jsonify(spc.client.auth_url)