from werkzeug.utils import redirect
from wtforms.ext.sqlalchemy.orm import model_form

from app import app, db

from flask import render_template, flash, url_for, request
from flask_login import login_required, logout_user

from app.views.incidentForm import IncidentForm
from app.models.incident import Incident


@app.route('/inc', methods=['GET', 'PUT', 'POST'])
@login_required
def incident():
    form = IncidentForm(request.form)
    form.mode = request.method
    form.url = 'incident'

    rid = request.args.get('id')
    record = None

    if form.validate_on_submit():
        record = form.processForm()
        return redirect('/viewpage-inc&h=' + record.id)
    else:
        record = Incident.query.get(rid)
        form.process(obj=record)
    form.flash_errors()

    return render_template('/inc/incidentForm.html', form=form, record=record)
