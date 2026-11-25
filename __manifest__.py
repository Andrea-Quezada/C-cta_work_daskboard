{
    'name': 'CTA Work Dashboard',
    'version': '17.0.1.0.0',
    'summary': 'Dashboard ejecutivo con permisos, gráficos y exportación',
    'category': 'Website',
    'author': 'CTA Work',
    'depends': [
        'base',
        'website',
        'account',
        'stock',
        'purchase',
        'mrp',
    ],
    'data': [
        'security/security.xml',
        'views/dashboard_templates.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
