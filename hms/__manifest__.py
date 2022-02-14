{
    'name': "hms",

    'summary': """
        This is Hospital Management System""",

    'description': """
        Odoo Day 1
    """,
    'author': "Aya Zeid",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_view.xml',
        'views/hms_doctor_view.xml',
        'views/hms_department_view.xml',
        'views/hms_customer_view.xml',
        'views/hms_patientlog_view.xml',
        'reports/report.xml',
        'reports/templates.xml'

    ],
}
