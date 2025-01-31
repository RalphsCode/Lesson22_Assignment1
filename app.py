"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)  # creating an instance of the Flask Class

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ponderosa@localhost/blogly'
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_ECHO'] = True

with app.app_context():
    connect_db(app)
    db.create_all()

app.config['SECRET_KEY'] = "RalphsCode123"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        # Display the new user form
        return render_template('new_user.html')
    else:
        # Process the new user form
        first = request.form['first_name']
        last = request.form['last_name']
        img_url = request.form['image_url']
        new_user = User(first_name=first, last_name=last, image_url=img_url)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'GET':
        return render_template('edit_user.html', user=user)
    else:
        first_name = request.form.get('first_name')
        last_name  = request.form.get('last_name')
        image_url = request.form.get('image_url')
        # If 1 or more fields are updated, update the record
        if first_name != '':
            user.first_name = first_name
        if last_name != '':
            user.last_name = last_name
        if image_url != '':
            user.image_url = image_url
        flash('+++ User has been updated +++')
        db.session.add(user)
        db.session.commit()
        return render_template('user.html', user=user)
    
@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.query.filter_by(id = user_id).delete()
    db.session.commit()
    flash(' >>> User has been deleted <<<')
    return redirect('/users')