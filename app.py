from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = '2b45e1d67fc43175cfae2c2553e5f6d0'  # Replace with your secret key

# Replace with your user database or authentication logic
users = {'pratham75': '123456', 'kumbhare': '486240', 'user45': '7878'}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/')
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
