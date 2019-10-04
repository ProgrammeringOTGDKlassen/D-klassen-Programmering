from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('formular.html')

@app.route("/modtag_data", methods=['POST'])
def modtag():
    modtaget_navn = request.form['navn']
    modtaget_email =request.form['email']
    return render_template("vis.html", navn = modtaget_navn, email = modtaget_email)

if __name__ == "__main__":
    app.run(debug=True)
