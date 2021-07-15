from flask_login import current_user, login_user, login_required


class Menu:
    items = [
        {
            'desc': 'Incident Management',
            'icon': '',
            'hidden': False,
            'items': [
                {
                    'desc': 'Manage Injuries',
                    'icon': 'view_list',
                    'link': '/viewpage-inc',
                    'hidden': False
                },
            ]
        },
        {
            'desc': 'Workforce',
            'icon': '',
            'hidden': False,
            'items': [
                {
                    'desc': 'Hours Worked',
                    'icon': 'view_list',
                    'link': '/rod',
                    'hidden': False
                },
                {
                    'desc': 'Employee Directory',
                    'icon': 'view_list',
                    'link': '/rod',
                    'hidden': False
                },
                {
                    'desc': 'User Administration',
                    'icon': 'view_list',
                    'link': '/rod',
                    'hidden': False
                },
            ]
        },
    ]
