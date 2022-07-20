from flask import Flask
from api.packages import packages_blueprint

# Create the app and register the blueprint containing the routing
APP = Flask(__name__)
APP.register_blueprint(packages_blueprint)
