from markupsafe import escape 
import datetime
from flask import Flask, abort, render_template, request, redirect, session, url_for

app = Flask(__name__)

#NOUVEAU CODE DU SITE
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def index():
    message="Please login"
    return render_template('index.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['username']=='Wonwoo'and session['password']== 'Gam3Bo1seventeen17796':
            return redirect(url_for('home')) 
        else:
            return redirect(url_for('login')) 
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('password',None)
    return redirect(url_for('index'))

#ANCIEN CODE DU CODE 
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/home/')
def home():
    return render_template('home.html', utc_dt=datetime.datetime.utcnow())

@app.route('/comments/')
def comments():
    comments = ['life is a soup and i am a fork ',
                'wonderfull',
                'Sona kitna sona hai ',
                'dayumm man:]'
                ]
    return render_template('comments.html', comments=comments)

@app.route('/capitalize/<word>/')
def capitalize (word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1+n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)




