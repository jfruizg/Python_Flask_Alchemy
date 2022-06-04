from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash
from models.model import Comment, User
from utils.db import db
import pandas as pd

excel = Blueprint('python_excel_routes', __name__)

@excel.route('/import_excel', methods=['POST', 'GET'])
def import_excel():
    return render_template("./excel/index.html")

@excel.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        file = request.form["upload_excel_file"]
        print(file)
        data = pd.read_excel(file)

        lista = []
        valores = data.values
        for row in valores:
            username = row[0]
            email = row[1]
            pasw = row[2]

            new_user = User(username, pasw, email)

            db.session.add(new_user)
            db.session.commit()

        return render_template("./excel/data.html", data = lista)


    return render_template()