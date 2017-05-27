from rest_framework import viewsets
from opal.core.views import json_response
from rest_framework.permissions import IsAuthenticated
from opal.models import Patient


class MirApi(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def dispatch(self, *args, **kwargs):
        self.name = kwargs.pop('name', 'pathway')
        self.incident_id = kwargs.get('incident_id', None)
        return super(MirApi, self).dispatch(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        Patient.objects.get(id=self.incident_id)

        return json_response({
            "title": {
                "text": {
                    "headline": "Sheppey Crossing Major Incident<br />3rd September 2013",
                    "text": "<p>Timeline of Sheppey Crossing incident</p>"
                }
            },
            "events": [
                {
                    "start_date": {
                        "month": "9",
                        "day": "3",
                        "year": "2013",
                        "hour": "7",
                        "minute": "15"
                    },
                    "text": {
                        "headline": "Incident occurs",
                        "text": "<p>High fog causes 150 vehicles to crash into each other over 10 minutes</p>"
                    }
                },
            ]
        })
