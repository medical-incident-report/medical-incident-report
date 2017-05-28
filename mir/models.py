"""
mir models.
"""
from django.db import models as fields
from opal.core.fields import ForeignKeyOrFreeText

from opal import models

"""
Core Opal models - these inherit from the abstract data models in
opal.models but can be customised here with extra / altered fields.
"""
class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.SymptomComplex): pass
class PatientConsultation(models.PatientConsultation): pass


YES_NO_CHOICES = (
    ('Yes', 'Yes',),
    ('No', 'No',),
)


class RegisterIncident(models.PatientSubrecord):
    _is_singleton = True

    incident_name = fields.CharField(max_length=255, blank=True)

    where_its_happend = fields.CharField(
        max_length=255, blank=True, null=True
    )

    countries = fields.ManyToManyField(
        models.Destination, related_name="incident_countries",
        verbose_name="In which countries did it happen?"
    )

class FirstEmergencyResponder(models.PatientSubrecord):
    _is_singleton = True

    date_time = fields.DateTimeField(
        null=True,
        blank=True
    )

    # one_common_number = fields.CharField(
    #     default="Yes",
    #     choices=YES_NO_CHOICES, max_length=256,
    #     verbose_name="Is there one common phone number for the emergency services?"
    # )

    # directly_referred = fields.CharField(
    #     default="Yes",
    #     choices=YES_NO_CHOICES,
    #     max_length=256,
    #     verbose_name="Can an emergency incident be referred directly by the EMS?"
    # )

    # voluntary = fields.TextField(
    #     null=True, blank=True,
    #     verbose_name="Which voluntary organisations can assist the EMS?"
    # )

    # authorisation_required = fields.CharField(
    #     choices=YES_NO_CHOICES, max_length=256,
    #     verbose_name="Do they require authorisation from the police?"
    # )

    # trauma_centres = fields.IntegerField(
    #     blank=True, null=True,
    #     verbose_name="Please enter the number of major trauma centres within the EMS catchment zone?"
    # )

    # trauma_units = fields.IntegerField(
    #     blank=True, null=True,
    #     verbose_name="Please enter the number of major trauma units within the EMS catchment zone?"
    # )

    # hospital_without_trauma_specialty = fields.IntegerField(
    #     blank=True, null=True,
    #     verbose_name="Please enter the number of hospitals without trauma specialty within the EMS catchment zone?"
    # )

    # triage_system = fields.CharField(
    #     default=False, choices=YES_NO_CHOICES, max_length=256,
    #     verbose_name="Is a prehospital on scene triage system being used daily on a national level?"
    # )

    # which_triage_system = fields.CharField(
    #     max_length=256, blank=True, null=True, choices=YES_NO_CHOICES,
    #     verbose_name="Please specify which prehospital on scene triage system is being used"
    # )

    # different_system = fields.CharField(
    #     max_length=256, blank=True, null=True, choices=YES_NO_CHOICES,
    #     verbose_name="Is the system used on a daily basis the same as the one used in a major incident"
    # )

    # different_system_description = fields.TextField(
    #     verbose_name="If not what is it?"
    # )

    cause_transport_industrial = fields.BooleanField(
        default=False,
        verbose_name = "Transport and industrial accident"
    )

    cause_extreme_weather = fields.BooleanField(
        default=False,
        verbose_name = "Extreme weather"
    )

    cause_fire = fields.BooleanField(
        default=False,
        verbose_name = "Fire"
    )

    cause_mass_gathering = fields.BooleanField(
        default=False,
        verbose_name = "Mass Gathering"
    )

    cause_explosive = fields.BooleanField(
        default=False,
        verbose_name = "Explosive"
    )

    cause_industrial_accident = fields.BooleanField(
        default=False,
        verbose_name = "Industrial accident"
    )

    cause_nuclear_radiological = fields.BooleanField(
        default=False,
        verbose_name = "Nuclear or radiological incident"
    )

    cause_biological = fields.BooleanField(
        default=False,
        verbose_name = "Biological"
    )

    cause_chemical = fields.BooleanField(
        default=False,
        verbose_name = "Chemical"
    )

    cause_other = fields.BooleanField(
        default=False,
        verbose_name = "Other / unknown"
    )

    specify_weather = fields.CharField(
        null=True,
        blank=True,
        choices=[("Avalance", "Avalanche"),
                     ("Flooding", "Flooding"),
                     ("Thunderstorm", "Thunderstorm"),
                     ("Hurricane", "Hurricaine"),
                     ("Extreme heat", "Extreme heat"),
                     ("Extreme cold", "Extreme cold"),
                     ("Other type of extreme weather. Please specify",
                          "Other types of extreme weather. Please specify")],
        verbose_name="Please specify the extreme weather that caused the incident",
        max_length=256
    )

    specify_cause = fields.TextField(
        null=True,
        blank=True,
        verbose_name="Please specify other mechanism/external factor that caused the incident"
    )

    coupled_to_another = fields.CharField(
        null=True,
        blank=True,
        choices=YES_NO_CHOICES,
        max_length=256,
        verbose_name="Is this incident coupled to another incident?"
    )

    specify_coupled = fields.TextField(
        null=True,
        blank=True,
        verbose_name="Please specify which other incident this major incident is coupled to"
    )

    location_urban = fields.BooleanField(
        default=False,
        verbose_name = "Urban area"
    )

    location_rural = fields.BooleanField(
        default=False,
        verbose_name = "Rural/countryside area"
    )

    location_maritime = fields.BooleanField(
        default=False,
        verbose_name = "Offshore/maritine (ocean, river, lake)"
    )

    location_mountain = fields.BooleanField(
        default=False,
        verbose_name = "Mountain"
    )

    location_road = fields.BooleanField(
        default=False,
        verbose_name = "Road"
    )

    location_airport = fields.BooleanField(
        default=False,
        verbose_name = "Airport"
    )

    location_education = fields.BooleanField(
        default=False,
        verbose_name = "Education facility"
    )

    location_public = fields.BooleanField(
        default=False,
        verbose_name = "Public facility"
    )

    location_healthcare = fields.BooleanField(
        default=False,
        verbose_name = "Health care facility"
    )

    location_building = fields.BooleanField(
        default=False,
        verbose_name = "Building"
    )

    location_gathering = fields.BooleanField(
        default=False,
        verbose_name = "Mass gathering"
    )

    location_other = fields.BooleanField(
        default=False,
        verbose_name = "Other / unknown"
    )

    specify_location = fields.TextField(
        null=True,
        blank=True,
        verbose_name="Please specify which other type of location of incident scene"
    )

class IncidentTimeline(models.PatientSubrecord):
    _is_singleton = True

    incident_occurs = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Time incident occurred"
    )

    first_ems_call = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Initial call to emergency services EOC"
    )

    first_ems_response = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First EMS response vehicle arrives on scene"
    )

    first_police_response = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First Police arrive on scene"
    )

    first_fire_response = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First Fire services arrive on scene"
    )

    med_commander = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Medical responder assumes the role of on-scene medical commander"
    )

    safety_assessment_start = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Medical responder begins to make an assessment of scene safety"
    )

    report_to_ems = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Medical responder communicates a situation report to EMS coordination centre"
    )

    resource_request = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Medical responder requests additional resources"
    )

    safety_action = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Medical responder initiates any safety related actions"
    )

    delegation = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Medical responder delegates responsibility for other tasks on-scene"
    )

    ems_officer_arrives = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First EMS officer arrives on scene"
    )

    ems_officer_commands = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First EMS officer assumes role of medical commander"
    )

    mi_declared = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="EMS declares a major incident"
    )

    summon_staff = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Summoning of additional medica staff to scene"
    )

    clearning_start = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Casualty Clearing Station established"
    )

    hospital_informed = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Hospital informed of major incident"
    )

    hospital_declares = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Hospital declares major incident"
    )

    first_patient_evacuated = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First patient evacuated from scene"
    )

    first_patient_arrives = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="First patient arrives at hospital"
    )

    medical_communication = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Communication between medical personell at the incident initiated"
    )

    task_force_communication = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Communication between different task forces (e.g. police, fire) initiated"
    )

    last_patient_evacuated = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Last patient evacuated from scene"
    )

    last_patient_arrives = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Last patient arrives at hospital"
    )

    mi_stand_down_ems = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Major incident stand down declared by EMS"
    )

    mi_stand_down_hospital = fields.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Major incident stand down declared by hospital"
    )
