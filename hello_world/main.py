from flask import Flask
from flask import render_template, request
app = Flask(__name__)
app.debug=True

@app.route("/", methods=['get','post'])
def login_view():
    msg = ''
    if request.method == 'POST':
        username = request.form["username"]
        passwd = request.form["passwd"]

        if username == 'kitsios' and passwd == 'pass':
            msg = "Username and password are correct"
        else:
            msg = "Username or password are incorrect"
    return render_template("form.html", message=msg)


if __name__ == "__main__":
    app.run()
