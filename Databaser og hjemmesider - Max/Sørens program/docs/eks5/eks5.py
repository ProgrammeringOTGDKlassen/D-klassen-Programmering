from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('main.html', text1 = "Første tekst", text2 = "Anden tekst")

@app.route("/side1")
def side1():
    return render_template('side1.html')

@app.route("/side2")
def side2():
    return render_template('side2.html')

@app.route("/side3")
def side3():
    return render_template('side3.html')
if __name__ == "__main__":
    app.run(debug=True)
