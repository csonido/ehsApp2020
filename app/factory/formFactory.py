from app import db
from flask import url_for


class DataSourceFactory:
    pages = {
        'inc': {
            'title': 'Injuries',
            'add_link': 'incident',
            'columns': [
                {'name': 'Incident Name', 'colname': 'i.incname', 'alias': 'incname'},
                {'name': 'Incident Date', 'colname': 'i.incdate', 'alias': 'incdate'},
                {'name': 'Full Description', 'colname': 'i.fullDesc', 'alias': 'fulldesc'},
                {'name': 'Edit',
                    'colname': """'javascript:callModalForm({url: "/inc?id=' || i.id || '", 
                    mode: "GET", modal: true});'""",
                    'alias': 'editbtn', 'action': True},
            ],
            'from': 'incident as i',
            'wherejoin': '1=1',
        }
    }

    @staticmethod
    def filters(code):
        page = DataSourceFactory.pages[code]

        if page['filters']:
            return page['filters']
        else:
            return []

    @staticmethod
    def create(code):
        page = DataSourceFactory.pages[code]
        dataset = {
            'title': page['title'],
            'add_link': page['add_link'],
            'headers': page['columns'],
        }

        with db.engine.connect() as conn:
            sql = 'SELECT '
            for i, col in enumerate(page['columns']):
                sql += (', \n' if i > 0 else '') \
                       + page['columns'][i]['colname'] \
                       + ' AS ' + page['columns'][i]['alias']
            sql += '\n FROM ' + page['from']
            sql += '\n WHERE ' + page['wherejoin']

            result = conn.execute(sql)
            dataset['rows'] = [dict(row) for row in result]

        return dataset


