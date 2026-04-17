from flask import Blueprint, render_template

main = Blueprint("main", __name__, template_folder="templates")

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/learn")
def learn():
    return render_template("learn.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/login")
def login():
    return "<h1>Login Page Coming Soon</h1>"

@main.route("/topic/<name>")
def topic_detail(name):
    return render_template("topic_detail.html", name=name)