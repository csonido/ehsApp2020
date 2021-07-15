from app import app, db
from app.factory.datasourceFactory import DataSourceFactory

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required


@login_required
@app.route('/viewpage-<code>')
def viewpage(code):
    dataset = DataSourceFactory.create(code)
    return render_template('viewpage.html',
                           dataset=dataset,
                           )
