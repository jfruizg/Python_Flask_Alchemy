from flask import Blueprint, render_template, request, redirect, url_for, make_response, session
from models.model import User
from utils.db import db


contact = Blueprint('python_contact_routes', __name__)

@contact.route('/')
def home():
    if 'username' in session:
        username = session['username']
        print(username)
        user = User.query.filter_by(username=username).first()
        return render_template('./user/index.html', contacts=user)
    else:
        return render_template('./user/login.html')

@contact.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('python_contact_routes.home'))

@contact.route('/new', methods=['POST'])
def add_contact():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    session['username'] = username

    new_user = User(username, password, email)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('python_contact_routes.home'))

@contact.route('/update/<id>', methods = ["POST", "GET"])
def update_contact(id):
    contact_p = User.query.get(id)
    return render_template('./user/update.html', contact = contact_p)

@contact.route('/delete/<id>')
def delete_contact(id):
    contact = User.query.get(id)

    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('python_contact_routes.home'))

@contact.route('/about')
def about_contact():
    return render_template('./user/about.html')

@contact.route('/cookie')
def cookie():
    response = make_response(render_template("./user.cookies.html"))
    response.set_cookie('custome_cookie', 'Eduardo')
    return response