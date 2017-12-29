from flask import Blueprint
from flask import render_template

about_page = Blueprint('about', __name__, template_folder='templates')


@about_page.route('/about')
def show():
    return render_template("about.html")
