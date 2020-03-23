from note_data import Database, User

from flask import Flask, request, g, render_template, session, redirect, url_for
from ast import literal_eval
import os, random, string, json

app = Flask(__name__)
key = "very secret string"
app.secret_key = key

with app.app_context():
    data = Database()


@app.teardown_appcontext
def close_connection(exception):
    data.close_connection()


def my_render(template, **kwargs):
    login_status = get_login_status()
    if login_status:
        return render_template(
            template, loggedin=login_status, user=session["currentuser"], **kwargs
        )
    else:
        return render_template(template, loggedin=login_status, user="", **kwargs)


def get_login_status():
    return "currentuser" in session


def get_user_id():
    if get_login_status():
        return session["currentuser"]
    else:
        return -1


def login_success(username, password):
    return data.login_success(username, password)


def check_same_password(password, re_password):
    if password == re_password:
        return True
    else:
        return False


def clean_dict_from_req_args(cluttered_dict):
    cluttered_dict = cluttered_dict[""].replace("'", '"')
    cluttered_dict = cluttered_dict[1:-1]
    info = json.loads(cluttered_dict)
    return info


def signup_success(username, firstname, lastname, email, password, re_password):
    if check_same_password(password, re_password):
        hashed_password = data.hash_password(password)
        # The last parameter is 1 because the user signing up will always be a Student. An admin will then be able to change that rank.
        u = User(username, firstname, lastname, email, hashed_password)
        if not data.signup_success(user=u):
            return False
        return True
    else:
        return False


@app.route("/")
@app.route("/login")
def index():
    return my_render("index.html", success=False, title="login")


@app.route("/login_profile", methods=["POST"])
def login():
    password = request.form["password"]
    username = request.form["username"]

    if login_success(username=username, password=password):
        # Create user object, store in session.
        session["currentuser"] = data.get_user_id(username)
        return redirect(f"/profile")
    else:
        session.pop("currentuser", None)
        return redirect(f"/")


@app.route("/logout")
def logout():
    session.pop("currentuser", None)
    return redirect(f"/")


@app.route("/signup")
def signup_site():
    return my_render("sign_up.html", title="signup")


@app.route("/profile")
def profile():
    return my_render("user_main.html", title="Student", success=True)


@app.route("/signup_profile", methods=["POST"])
def signup():
    username = request.form["username"]
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    password = request.form["password"]
    re_password = request.form["re_password"]

    if signup_success(
        username=username,
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password,
        re_password=re_password,
    ):
        return index()
    else:
        session.pop("currentuser", None)
        return my_render("sign_up.html", success=False)


@app.route("/edit_note")
def edit_note():
    return my_render("edit_note.html")


@app.route("/remove_note")
def remove_note():
    return redirect("/showclass?='1'")


@app.route("/showclass")
def showclass():
    print(clean_dict_from_req_args(request.args))
    return my_render("class_page.html", success=True)


@app.route("/take_notes")
def take_notes():
    return my_render("note_writer.html")


@app.route("/submit_note", methods=["POST"])
def submit_note():
    return redirect("/profile")


@app.route("/submit_note_edit", methods=["POST"])
def submit_note_edit():
    return redirect("/profile")


@app.route("/read_note")
def read_note():
    print(clean_dict_from_req_args(request.args))
    return my_render("read_note.html", success=True)


if __name__ == "__main__":
    with app.app_context():
        data = Database()

    app.run(debug=True)