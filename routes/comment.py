from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash
from models.model import Comment, User
from utils.db import db
import pandas as pd

comment = Blueprint('python_comment_routes', __name__)

@comment.route('/home_comment')
def home():

    return render_template('./comment/new.html')

@comment.route('/new_comment',methods=['POST'])
def new():
    if 'username' in session:
        username = session['username']
        user = User.query.filter_by(username=username).first()
        user_id = user.id

        text = request.form['text']

        new_comment = Comment(user_id, text)

        db.session.add(new_comment)
        db.session.commit()
        comments_user = Comment.query.filter_by(user_id=user_id).all()

        return render_template('./user/index.html')

@comment.route('/show')
def show():
    if 'username' in session:
        username = session['username']
        user = User.query.filter_by(username=username).first()
        user_id = user.id

        comments_user = Comment.query.filter_by(user_id=user_id).all()

        return render_template('./comment/show.html', comments=comments_user)

@comment.route('/delete/<id>')
def delete_comment(id):
    comment = Comment.query.get(id)

    db.session.delete(comment)
    db.session.commit()

    return render_template('./user/register.html')






