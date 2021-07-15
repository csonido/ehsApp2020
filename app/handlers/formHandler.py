from abc import ABC, abstractmethod
from flask_wtf import FlaskForm


class FormHandler(ABC):
    @abstractmethod
    def handle(self, form: FlaskForm):
        return {}

    @abstractmethod
    def validate_form(self, form: FlaskForm):
        return True


