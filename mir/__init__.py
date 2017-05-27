"""
mir - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/mir/routes.js',
        'js/opal/controllers/discharge.js',
        'opal/services/patient_summary.js',
        'opal/services/patient_detail.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/mir/flow.js',
    ]
