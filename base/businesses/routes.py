from flask import blueprint, request, url_for, render_template

bus = blueprint("bus", __name__)


@bus.route("/")
def index():
	return render_template("index.html")
