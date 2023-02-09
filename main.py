from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # check if the username and password match
        if username == "admin" and password == "secret":
            return redirect(url_for("dashboard"))
        else:
            return "Wrong credentials, try again."
        
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "Welcome to the dashboard, admin."

if __name__ == "__main__":
    app.run(debug=True)
