from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'khatarnak_secret_key'

users = {}

@app.route('/')
def home():
    if 'user' in session:
        return f"<h1>Welcome, {session['user']} 🧠</h1><br><a href='/logout'>Logout</a>"
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            error = "Invalid Credentials ❌"
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            msg = "User already exists ⚠️"
        else:
            users[username] = password
            msg = "Registered successfully ✅"
    return render_template('register.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
