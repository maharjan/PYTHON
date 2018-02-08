from flask import *
import os

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return inner()

@app.route('/login', methods=['GET','POST'])
def admin_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['logged_in']=True
    else:
        flash('Invalid login credential!')
    # return render_template("login.html", error = error)
    return home()

@app.route('/main')
def inner():
    return render_template("main.html")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return home()

if __name__ == "__main__":
    app.secret_key =os.urandom(12)
    app.run(debug=True, host='localhost', port=8090) 