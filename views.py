"""
Defines views for Flask project site, represented
as functions here. Includes decorator for handling
routing required login credentials. Configuration
for Flask app object imported from _config module,
in same directory as this file.
"""
import sqlite3
from functools import wraps
from flask import Flask, flash, redirect, \
    render_template, request, session, url_for

app = Flask(__name__)
app.config.from_object('_config')

def connect_db():
    """Connect to blog database."""
    return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(func):
    """Decorator function for handling certain
    routes requiring login credentials."""
    @wraps(func)
    def wrap(*args, **kwargs):
        """Nested function checking for logged_in key
        inside session object."""
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('Login required before viewing page.')
            return redirect(url_for('login'))
    return wrap 

@app.route('/', methods=['GET', 'POST'])
def login():
    """Login page. Checks for correct credentials."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again' 
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('main'))  
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """Logout view, redirects back to login page."""
    session.pop('logged_in', None)  # removes 'logged_in'
    flash('Logging out...')
    return redirect(url_for('login'))

@app.route('/main')
@login_required
def main():
    """If logged in, shows existing posts and allows
    for adding more posts in given form."""
    with connect_db() as blog_db:
        cur_dict = blog_db.execute('select * from blog_posts').fetchall()  # retrieve all posts
        posts = [dict(title=row[0], post=row[1]) for row in cur_dict]
    return render_template('main.html', posts=posts)

@app.route('/add', methods=['POST'])
@login_required
def add():
    """View for adding posts, provided valid fields."""
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required. Please try again.")
        return redirect(url_for('main'))
    else:
        with connect_db() as blog_db:
            blog_db.execute('insert into blog_posts (title, post) values (?, ?)', \
                                [title, post])
            blog_db.commit()
        flash("New entry successfully posted!")
        return redirect(url_for('main'))
 
