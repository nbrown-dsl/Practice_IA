from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    names =["Noah", "Charles", "Anastasia", "Dot"]
    return render_template("about.html", names=names)

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")
    
#only allowed to come here if you have submitted a form to here
@app.route('/form', methods=["POST"])
def form():
    first_name = subscribe
    return render_template("form.html", first_name=first_name)
