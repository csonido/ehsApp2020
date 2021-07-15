import re
import bs4
import numpy as np
import xml.dom.minidom

from http.client import HTTPConnection
from flask_wtf import FlaskForm
from werkzeug.datastructures import FileStorage

from app.handlers.formHandler import FormHandler


class RodHandler(FormHandler):
    def handle(self, form: FlaskForm):
        # clean url
        url = form.data['url']
        upload_data = form['docupload'].data

        if upload_data is not None:
            return {
                'response': self.__processPDF__(upload_data),
                'status': '200',
                'reason': 'OK'
            }
        elif url is not None:
            conn = HTTPConnection(url)
            conn.request("GET", "/")
            response = conn.getresponse()
            data = response.read()
            return {
                'response': self.__processXML__(data),
                'status': response.status,
                'reason': response.reason
            }

    def __processPDF__(self, fileStorage: FileStorage):
        fileReader = None # pypdf2.PdfFileReader(fileStorage)
        return fileReader

    def __processXML__(self, text):
        soup = bs4.BeautifulSoup(text)

        final = ''
        irrelevant_tags = ['style', 'script', 'head', 'title', 'meta', 'document']
        for tag in irrelevant_tags:
            [t.extract() for t in soup(tag)]
        for s in soup.find_all():
            final += s.get_text()
        return final


