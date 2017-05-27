from mir import models

from pathway.pathways import (
    PagePathway, RedirectsToPatientMixin
)


class MajorIncidentPathway(RedirectsToPatientMixin, PagePathway):
    _is_singleton = True
    icon = "fa fa-sign-out"
    display_name = "Add Incident"
    finish_button_text = "Add Incident"
    finish_button_icon = "fa fa-sign-out"
    slug = "majorincident"
    steps = (
        models.RegisterIncident,
    )


class FirstEmergencyResponder(RedirectsToPatientMixin, PagePathway):
    _is_singleton = True
    icon = "fa fa-sign-out"
    display_name = "First Emergency Responder"
    finish_button_text = "Done"
    finish_button_icon = "fa fa-sign-out"
    slug = "first_emergency_responder"
    steps = (
        models.FirstEmergencyResponder,
    )
