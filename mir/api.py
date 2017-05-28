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
        field_names = ["incident_occurs",
                           "first_ems_call",
                           "first_ems_response",
                           "first_police_response",
                           "first_fire_response",
                           "med_commander",
                           "safety_assessment_start",
                           "report_to_ems",
                           "resource_request",
                           "safety_action",
                           "delegation",
                           "ems_officer_arrives",
                           "ems_officer_commands",
                           "mi_declared",
                           "summon_staff",
                           "clearning_start",
                           "hospital_informed",
                           "hospital_declares",
                           "first_patient_evacuated",
                           "first_patient_arrives",
                           "medical_communication",
                           "task_force_communication",
                           "last_patient_evacuated",
                           "last_patient_arrives",
                           "mi_stand_down_ems",
                           "mi_stand_down_hospital"
                           ]
        result = {
            "title": {
                "text": {
                    "headline": self.register_incident.incident_name,
                    }
                },
            "events": []
            }
        for field_name in field_names:
            field = getattr(self.incident_timeline, field_name)
            if field is not None:
                field_data = {
                    "start_date": {
                        "month": field.month,
                        "day": field.day,
                        "year": field.year,
                        "hour": field.hour,
                        "minute": field.minute
                    },
                    "text": {
                        "headline": self.incident_timeline._get_field_title(field_name)
                    }
                }
                result["events"].append(field_data)
        return json_response(result)
