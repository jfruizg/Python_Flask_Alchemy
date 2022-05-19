from flask import Blueprint, render_template, request, redirect, url_for
from models.contact import Contact
from utils.db import db


contact = Blueprint('python_contact_routes', __name__)

@contact.route('/')
def home():
    all_contact = Contact.query.all()
    return render_template('./client/index.html', contacts = all_contact)

@contact.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    print(new_contact)

    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('python_contact_routes.home'))

@contact.route('/update/<id>', methods = ['POST', 'GET'])
def update_contact(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        return redirect(url_for('python_contact_routes.home'))

    return render_template('./client/update.html', contact = contact)

@contact.route('/delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)

    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('python_contact_routes.home'))

@contact.route('/about')
def about_contact():
    return render_template('./client/about.html')