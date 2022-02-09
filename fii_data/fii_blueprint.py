from flask import Blueprint, jsonify, request, Response
from .utils import dict_to_xml

fii_blueprint = Blueprint('fii_blueprint', __name__)

@fii_blueprint.route('/fii/')
def fii_root():
    return f'Usage /fii/TICKER'

@fii_blueprint.route('/fii/<ticker>')
def get_ticker_info(ticker:str):
    format = request.args.get('format', default='JSON', type=str)
    print('-*'*20)
    print(f'format query string: {format}')
    print('-*'*20)

    ticker_info = get_fii_info(ticker.upper())

    if format.strip().upper() == 'XML':
        xml = dict_to_xml(ticker_info)
        return Response(xml, mimetype='text/xml')

    return jsonify(ticker_info)