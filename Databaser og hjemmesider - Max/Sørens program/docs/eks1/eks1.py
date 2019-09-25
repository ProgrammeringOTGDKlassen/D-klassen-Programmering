from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('eks1.html')
@app.route('/about') #Øvelse1
def about(): #Øvelse1
    return render_template('about.html') #Øvelse1

if __name__ == "__main__":
    app.run(debug=True)
