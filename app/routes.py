from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/")
def about():
    return render_template("about.html")

@main.route("/")
def base():
    return render_template("base.html")

@main.route("/")
def contact():
    return render_template("contact.html")

@main.route("/")
def learn():
    return render_template("learn.html")

@main.route("/")
def login():
    return render_template("login.html")

@main.route("/")
def project():
    return render_template("project.html")