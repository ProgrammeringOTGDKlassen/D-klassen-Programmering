from flask import Flask, request, g, render_template, session, redirect, url_for
from idea_datalayer import IdeaData

app = Flask(__name__)
app.secret_key = 'very secret string'

data = None

@app.teardown_appcontext
def close_connection(exception):
    data.close_connection()

"""
Denne funktion sørger for at pakke den template, der skal vises,
ind i nogle standard-ting, f.eks. loginstatus.

my_render bør kaldes i stedet for at kalde render_template direkte.
"""
def my_render(template, **kwargs):
    login_status = get_login_status()
    if login_status:
        return render_template(template, loggedin=login_status, user = session['currentuser'], **kwargs)
    else:
        return render_template(template, loggedin=login_status, user = '', **kwargs)

@app.route("/")
@app.route('/index')
def index():
    return redirect(url_for('.home'))

def get_login_status():
    return 'currentuser' in session


@app.route("/")
@app.route("/home")
def home():
    return my_render('home.html')

@app.route("/register")
def register():
    return my_render('register.html', success= True, complete = True)

@app.route("/login")
def login():
    return my_render('login.html', success = True)

@app.route("/logout")
def logout():
    session.pop('currentuser', None)
    return my_render('home.html')


@app.route("/about")
def about():
    return my_render('about.html', title='Om OnTrack')

@app.route("/contact")
def contact():
    return my_render('contact.html', title='Kontakt')

def login_success(user, pw):
    return data.login_success(user,pw)

def register_success(user, pw, email):
    return data.register_user(user, pw, email)

@app.route('/register_user', methods=['POST'])
def register_user():
    pw = request.form['password']
    user = request.form['username']
    email = request.form['email']

    if register_success(user, pw, email):
        #Create user object, store in session
        session['currentuser'] = data.get_user_id(user)
        return my_render('home.html')
    else:
        session.pop('currentuser', None)
        if len(pw) == 0 or len(user) == 0:
            return my_render('register.html', success = False, complete = False)
        else:
            return my_render('register.html', success = False, complete = True)


@app.route('/login_user', methods=['POST'])
def login_user():
    pw = request.form['password']
    user = request.form['username']

    if login_success(user, pw):
        #Create user object, store in session.
        session['currentuser'] = data.get_user_id(user)
        return my_render('home.html')
    else:
        session.pop('currentuser', None)
        return my_render('login.html', success = False)

if __name__ == "__main__":
    with app.app_context():
        data = IdeaData()

    app.run(debug=True)
