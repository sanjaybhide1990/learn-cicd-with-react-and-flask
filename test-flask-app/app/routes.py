# API endpoints/Routes

from flask import Blueprint, jsonify
from .models import TestDB

main_bp = Blueprint('main', __name__)

@main_bp.route('/testRoute', methods=['GET'])
def test_route(): 
    messages = TestDB.query.all()
    output = [{'message': m.message} for m in messages]
    return jsonify(output)