from flask import Blueprint, render_template, request
from models.contact import Task
from utils.db import db


task = Blueprint('python_routes', __name__)

@task.route('/task_home')
def home():
    return render_template('./category/index.html')

@task.route('/task_new', methods=['POST'])
def add_contact():
    title = request.form['title']
    description = request.form['description']
    contact_id = request.form['contact_id']

    new_task = Task(title, description, contact_id)

    print(new_task)

    db.session.add(new_task)
    db.session.commit()

    return "save task"

@task.route('/update')
def update_contact():
    return "update contact"

@task.route('/delete')
def delete_contact():
    return "delete contact"

@task.route('/about')
def about_contact():
    return render_template('./client/about.html')