import re
from flask import Flask
from flask_cors import CORS

APP = Flask(__name__)

API_PREFIX = '/api/v1'
API_DOMAIN = '/packages'

# Allow CORS on every origin TODO: Maybe remove later
CORS(APP, resources={r"/api/*": {"origins": "*"}})

# TODO: Move to data layer
statusfile = 'status'
filecontents = ''

with open(statusfile, 'r', encoding="utf8") as statcontent:
    filecontents = statcontent.read()


# find all the matches
matches = re.findall(r'(?<=Package: )\w+.+', filecontents)

print(matches)