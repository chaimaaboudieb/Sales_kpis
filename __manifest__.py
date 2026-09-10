{
    'name': 'Sales KPI',
    'version': '1.0',
    'summary': 'Suivi des performances commerciales',
    'description': """
        Module de suivi des KPI commerciaux.
        Les données sont saisies manuellement.
    """,
    'author': 'Transformatek Exercise',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/commercial_views.xml',
        'views/sales_kpi_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}