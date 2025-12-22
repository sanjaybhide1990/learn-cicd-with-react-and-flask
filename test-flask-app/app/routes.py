# API endpoints/Routes

from flask import Blueprint, abort, jsonify
from .models import TestDB

main_bp = Blueprint('main', __name__)

@main_bp.route('/testRoute', methods=['GET'])
def test_route(): 
    return 'Hello There'

@main_bp.route('/getAllMessages',methods=['GET'])
def get_all_messages():
    messages = TestDB.query.all()
    output = [{'message': m.message} for m in messages]
    return jsonify(output)

@main_bp.route('/getMessage/<int:id>',methods=['GET'])
def get_message_by_id(id):
    get_message_by_id = TestDB.query.get(id)
    if get_message_by_id is None:
        abort(404, description="Record not found")
    return jsonify({'id': get_message_by_id.id,
                    'message': get_message_by_id.message})