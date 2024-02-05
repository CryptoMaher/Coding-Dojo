from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Micheal', 'last_name' : 'Choi' },
        {'first_name' : 'John', 'last_name' : 'Sup' },
        {'first_name' : 'Mark', 'last_name' : 'Gui' },
        {'first_name' : 'KB', 'last_name' : 'Tonel' },
    ]
    return render_template("index.html" ,users=users)


if __name__=="__main__":
    app.run(debug=True)