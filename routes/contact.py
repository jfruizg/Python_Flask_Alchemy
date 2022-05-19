from flask import Blueprint, render_template, request
from models.contact import Contact
from utils.db import db


contact = Blueprint('python_routes', __name__)

@contact.route('/')
def home():
    return render_template('./client/index.html')

@contact.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    print(new_contact)

    db.session.add(new_contact)
    db.session.commit()

    return "save contact"

@contact.route('/update')
def update_contact():
    return "update contact"

@contact.route('/delete')
def delete_contact():
    return "delete contact"

@contact.route('/about')
def about_contact():
    return render_template('./client/about.html')