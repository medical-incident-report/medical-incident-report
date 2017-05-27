"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from mir import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'
    template_name = 'patient_lists/mir_list.html'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()
