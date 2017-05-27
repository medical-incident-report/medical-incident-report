from rest_framework import viewsets
from opal.core.views import json_response
from rest_framework.permissions import IsAuthenticated
from opal.models import Patient

class MirApi(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def dispatch(self, *args, **kwargs):
        self.name = kwargs.pop('name', 'pathway')
        self.incident_id = kwargs.get('incident_id', None)
        self.patient = Patient.objects.get(id=self.incident_id)
        self.register_incident = self.patient.registerincident_set.get()
        self.incident_timeline = self.patient.incidenttimeline_set.get()
        return super(MirApi, self).dispatch(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        return json_response({
    "title": {
        "text": {
          "headline": self.register_incident.incident_name,
        }
    },
    "events": [
      {
        "start_date": {
          "month": self.incident_timeline.incident_occurs.month,
          "day": self.incident_timeline.incident_occurs.day,
          "year": self.incident_timeline.incident_occurs.year,
		  "hour": self.incident_timeline.incident_occurs.hour,
		  "minute": self.incident_timeline.incident_occurs.minute
		  
        },
        "text": {
          "headline": self.incident_timeline._get_field_title("incident_occurs")
        }
      }
    ]
})
