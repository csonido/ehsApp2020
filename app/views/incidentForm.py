from flask import flash, session

from app import db
from app.models.incident import Incident
from app.util.ehsbaseform import EHSBaseForm
from wtforms import StringField, MultipleFileField, TextAreaField, DateField


class IncidentForm(EHSBaseForm):
    incname = StringField('Incident Name', validators=[])
    incdate = DateField('Date Of Occurrence', format='%b %d, %Y', validators=[])
    fulldesc = TextAreaField('Full Description', validators=[])
    docs = MultipleFileField('Attachments', validators=[])

    def __init__(self, formdata=None):
        super(EHSBaseForm, self).__init__(formdata)
        self.form = None

    def processForm(self, request):
        record = Incident()
        self.populate_obj(record)

        if request.method.upper() == 'POST':
            db.session.add(record)
        if request.method.upper() == 'PUT':
            db.session.commit()

        self.flash_errors()
        return record
