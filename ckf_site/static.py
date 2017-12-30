from flask import Blueprint, send_from_directory

static_page = Blueprint('statics', __name__, template_folder='templates')


@static_page.route('/js/<path:path>')
def basic_js(path):
    return send_from_directory('js', path)


@static_page.route('/favicon')
def favicon():
    return send_from_directory('static', 'favicon.ico')
