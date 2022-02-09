from flask import Blueprint, jsonify

root_blueprint = Blueprint('root_blueprint', __name__)

@root_blueprint.route('/')
def root():
    return jsonify({'message': 'Usage: /fii/TICKER'})
