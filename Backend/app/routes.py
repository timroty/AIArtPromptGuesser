from flask import Blueprint, request, jsonify
from .supabase import Supabase
from .controllers.art import Art as art_controller

bp = Blueprint('api', __name__)
spc = Supabase()

@bp.route('/image', methods=['GET'])
def image():
    controller = art_controller()
    result = controller.get_random_art_piece()  
    data = {'id': result.id, 'reference_url': result.reference_url}
    return jsonify(data)

@bp.route('/image/<id>', methods=['GET'])
def image_id(id):
    controller = art_controller()
    result = controller.get_art_piece_by_id(id)  
    if result is not None:
        data = {'id': result.id, 'reference_url': result.reference_url}
        return jsonify(data)
    else:
        data = {'id': None, 'reference_url': None}
        return jsonify(data)

@bp.route('/image/guess', methods=['POST'])
def image_guess():
    body = request.json
    controller = art_controller()
    result = controller.guess_art_prompt(body['id'], body['guess'])  
    return jsonify(result)

@bp.route('/art/<id>', methods=['GET'])
def art_id(id):
    controller = art_controller()
    result = controller.get_art_piece_by_id(id)  
    if result is not None:
        return result.jsonify()
    else:
        return jsonify(None)