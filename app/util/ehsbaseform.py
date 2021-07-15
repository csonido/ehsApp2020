from flask import flash
from flask_wtf import FlaskForm


class EHSBaseForm(FlaskForm):
    def __init__(self):
        super(FlaskForm, self).__init__()
        self.form = None

    def process_form(self, request):
        raise NotImplementedError("Please Implement this method")

    def from_model(self, model):
        mkeys = [k for k in model.__dict__.keys()]
        for field in self._fields:
            if field in mkeys:
                self[field] = model[field]

    def flash_errors(self):
        for err in self.errors.items():
            for msg in err[1]:
                flash(self[err[0]].label.text + ": " + msg, 'error')

