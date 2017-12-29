from flask import Blueprint
from flask import render_template

home_page = Blueprint('home', __name__, template_folder='templates')


@home_page.route('/')
def show():
    return render_template("home.html", name="Carling")
