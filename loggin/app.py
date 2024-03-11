from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
# We could save the session data in a database and more, but here we do it in the file system
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    # If there's no name in the session (you're not logged in)
    if not session.get("name"):
        return redirect("/login")
    # If you are logged 
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # If the information was sent by a form via POST    
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)  