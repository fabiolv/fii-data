from flask import Flask
from .root_blueprint import root_blueprint
from .fii_blueprint import fii_blueprint
from .fii_com_br_blueprint import fii_com_br_blueprint

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    # app.config.from_object(config_object)
    app.register_blueprint(root_blueprint)
    app.register_blueprint(fii_com_br_blueprint)

    return app