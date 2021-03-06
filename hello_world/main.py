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

        if username == 'kitsios' and passwd == 'password':
            msg = "Username and password are correct"
            print(msg) 
            return render_template("index.html", message=msg)
        else:
            msg = "Username or password are incorrect"
            print(msg) 
            return render_template("wrong.html", message=msg)
           
    return render_template("form.html", message=msg)


if __name__ == "__main__":
    app.run()
