from werkzeug.utils import redirect

from app import app

from flask import render_template, flash, url_for
from flask_login import login_required, logout_user

from app.handlers.rodHandler import RodHandler
from app.views.rodForm import RODForm
from app.util.menu import Menu


@app.context_processor
def include_menu():
    return {'menu': Menu.items}


@app.route('/rod', methods=['GET', 'POST'])
@login_required
def rod():
    form = RODForm()
    output = None

    if form.validate_on_submit():
        output = RodHandler().handle(form)
    return render_template('read_on_demand/rod.html', title='Read On-Demand', form=form, output=output)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
