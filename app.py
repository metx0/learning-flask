from flask import Flask, render_template, request

app = Flask(__name__)

# we gonna write the code that decides what to show (what to answer), based on the browser's request

# code that the server will execute when a user visits the default page
@app.route("/")
def index():
    # get the value of the key 'name'. If there's no key like 'name', it uses 'world' as a default value
    # name = request.args.get("name", "world")
    return render_template("index.html")


# code that will execute when a user visits the route "/form"
@app.route("/user-info")
def form():
    return render_template("user_info.html", name=request.args.get("name", "world"))


if __name__ == "__main__":
    app.run(debug=True)