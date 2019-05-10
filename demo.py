from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def HelloWorld():

    if request.method == "POST":
        name = request.form.get("enterName")

    return render_template("main.html", name=name)

@app.route('/page')

def page():
    return render_template("page.html")

