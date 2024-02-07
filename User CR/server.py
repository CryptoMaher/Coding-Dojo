from flask import Flask, render_template, resquest, redirect 

from users import User

app = Flask(__name__)

app.secret_key="Benny bob wuz heer."

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

    @app.route('users/new')
    def new():
        return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(resquest.form)
    User.save(request.form)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)