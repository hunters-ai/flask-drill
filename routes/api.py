from flask import Blueprint, send_from_directory

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return send_from_directory('static', 'index.html')
