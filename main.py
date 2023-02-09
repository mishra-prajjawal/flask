from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

# Create a fake database to store the user credentials
users = {
    'username': 'password'
}

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('secret'))
        else:
            return 'Invalid Login'
    return render_template('login.html')

@app.route('/secret')
def secret():
    return 'You have logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)

