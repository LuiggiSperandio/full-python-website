from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/stringPage')
def home():
    return render_template("home.html")