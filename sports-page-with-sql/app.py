from flask import Flask, render_template, request

app = Flask(__name__)

# Supported sports
SPORTS = ["Basketball", "Soccer", "Baseball"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    # Save the key-value pairs
    name = request.form.get("name")
    sport = request.form.get("sport")

    # There's an error if the name is in blank or if the sport is not supported
    if sport not in SPORTS or not name:
        return render_template("failure.html")

    # REGISTRANTS[name] = sport

    return render_template("success.html", user_name=name)  

# Here we will show all the registrants and their sports
@app.route("/registrants")
def show_registrants():
    return render_template("registrants.html")

if __name__ == "__main__":
    app.run(debug=True)  