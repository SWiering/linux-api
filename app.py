from flask import Flask
from api.packages import packages_blueprint

APP = Flask(__name__)
APP.register_blueprint(packages_blueprint, url_prefix='/api/v1/packages')
