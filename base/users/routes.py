from flask import Blueprint, request, url_for, redirect, render_template


user = Blueprint("user", __name__)


@user.route("/signin")
def signin():
    return render_template("signin.html")

@user.route("/signup")
def signup():
    return render_template("about.html")

@user.route("/user_profile")
def profile():
    return render_template("contact.html")

@user.route("/notifications")
def notifications():
    return "Notifications Page"
