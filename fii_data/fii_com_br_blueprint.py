from flask import Blueprint, jsonify, request, Response
from .fii_com_br import get_fii_info
from .utils import dict_to_xml

fii_com_br_blueprint = Blueprint('fii_com_br_blueprint', __name__)

@fii_com_br_blueprint.route('/fii/')
def fii_root():
    return f'Usage /fii/TICKER'

@fii_com_br_blueprint.route('/fii/<ticker>')
def get_ticker_info(ticker:str):
    format = request.args.get('format', default='JSON', type=str)
    print('-*'*20)
    print(f'---> Request for /fii/{ticker}')
    print(f'format query string: {format}')
    print('-*'*20)

    ticker_info = get_fii_info(ticker.upper())

    if format.strip().upper() == 'XML':
        xml = dict_to_xml(ticker_info)
        return Response(xml, mimetype='text/xml')

    return jsonify(ticker_info)