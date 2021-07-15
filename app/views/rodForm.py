from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField


class RODForm(FlaskForm):
    url = StringField('Link to text', validators=[])
    docupload = FileField('Upload PDF', validators=[])
    submit = SubmitField('Process')
