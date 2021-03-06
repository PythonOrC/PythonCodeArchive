from flask import Flask, render_template, url_for, request, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'password'
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        session['user'] = user
        session.permanent = True
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f'<p>{user}</p>'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)