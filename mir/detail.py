from opal.core import detail
from django.conf import settings


class Incident(detail.PatientDetailView):
    display_name = "Incident"
    order = 5
    template = "detail/incident.html"
