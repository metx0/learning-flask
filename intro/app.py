from flask import Flask, render_template, request

app = Flask(__name__)

# "/" is the default page of your application. Like "localhost:5000/"
# It will handle both POST and GET methods
@app.route("/", methods=["GET", "POST"])
def index():
    # We will return different things, according to the request received

    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        # We use request.form to recover information sent via POST
        return render_template("user_info.html", name=request.form.get("name", "world"))

if __name__ == "__main__":
    app.run(debug=True)