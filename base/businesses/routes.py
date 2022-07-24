from flask import Blueprint, request, url_for, render_template

bus = Blueprint("bus", __name__)


@bus.route("/businesses")
def index():
	return render_template("index.html")
