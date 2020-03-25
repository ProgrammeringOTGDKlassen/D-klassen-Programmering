from note_data import Database, User
from API.class_classifier_model import TextClassifierModel

from flask import Flask, request, g, render_template, session, redirect, url_for
from ast import literal_eval
import os, random, string, json

app = Flask(__name__)
key = "very secret string"
app.secret_key = key

class_model = TextClassifierModel()

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
    # Get general class info
    classes_info = data.get_classes_info()
    # Get amount of notes in each class for current user
    num_notes_in_class_dict = data.get_num_notes_in_class(session["currentuser"])
    for i, class_info in enumerate(classes_info):
        i += 1
        class_info["num_notes"] = num_notes_in_class_dict[f"{i}"]

    return my_render(
        "user_main.html", title="Student", success=True, classes_info=classes_info,
    )


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
    note_info = clean_dict_from_req_args(request.args)
    return my_render("edit_note.html", note_info=note_info)


@app.route("/remove_note")
def remove_note():
    note_info = clean_dict_from_req_args(request.args)
    data.remove_note(note_info["note_id"], session["currentuser"])
    return redirect(f"/showclass?='{note_info['class_id']}'")


@app.route("/showclass")
def showclass():
    class_id = clean_dict_from_req_args(request.args)
    class_info = data.get_class_info(class_id)
    notes = data.get_notes_in_class(session["currentuser"], class_id)
    return my_render(
        "class_page.html", success=True, class_info=class_info, notes=notes
    )


@app.route("/take_notes")
def take_notes():
    return my_render("note_writer.html")


@app.route("/get_class_prediction", methods=["GET"])
def get_class_prediction():
    cluttered_dict = request.args
    body = cluttered_dict[""].replace("'", '"')
    class_model.prepare_data(body)
    prediction = class_model.predict_class()
    class_name = data.get_class_name(prediction)
    other_classes = data.get_other_class_names(class_name)
    class_names = {
        "class_name": class_name,
        "other_classes1": other_classes[0],
        "other_classes2": other_classes[1],
    }
    return class_names


@app.route("/submit_note", methods=["POST"])
def submit_note():
    subject = request.form["subject"]
    body = request.form["body"]
    class_name = request.form["class_name"]
    class_id = data.get_class_id_from_name(class_name)
    data.submit_note(session["currentuser"], class_id, subject, body)

    return redirect("/profile")


@app.route("/submit_note_edit", methods=["POST"])
def submit_note_edit():
    subject = request.form["subject"]
    body = request.form["body"]
    note_id = request.form["note_id"]
    data.edit_note(note_id, session["currentuser"], subject, body)
    return redirect(f"/read_note?='{note_id}'")


@app.route("/read_note")
def read_note():
    note_id = clean_dict_from_req_args(request.args)
    note_info = data.get_note_info(note_id, session["currentuser"])
    class_info = data.get_class_info(note_info["class_id"])
    return my_render(
        "read_note.html", success=True, note_info=note_info, class_info=class_info
    )


if __name__ == "__main__":
    with app.app_context():
        data = Database()

    app.run(debug=True)
