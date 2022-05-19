from flask import Blueprint, render_template, request

contact = Blueprint('python_routes', __name__)

@contact.route('/')
def home():
    return render_template('./client/index.html')

@contact.route('/new', methods=['POST'])
def add_contact():
    print(request.form['fullname'])
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