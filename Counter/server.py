from flask import Flask, render_template, session, redirect 
import random

app = Flask(__name__)

app.secret_key="Benny bob wuz heer."

@app.route('/')
def index():
    if "counter" not in session
    session["count"] = 0
    session['count'] += 1

    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)