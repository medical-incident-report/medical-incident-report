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

YES_NO_UKNOWN_CHOICES = (
    ('Yes', 'Yes',),
    ('No', 'No',),
    ('Unknown', 'Unknown',),
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


class IncidentPlanQuestions(models.PatientSubrecord):
    """ These questions are asked to all
        Bronze, Silver and Gold Advisors
    """
    prehospital_major_incident_plan = fields.TextField(
        verbose_name="Please Enter the pre-hospital major incident response if one exists?"
    )

    actual_response = fields.TextField(
        verbose_name="ow did your actual response differ to the plan and what was the consequence of that?"
    )


class EmsBackground(models.PatientSubrecord):
    ems_coordinating_centre_exists = fields.CharField(
        null=True,
        blank=True,
        choices=YES_NO_CHOICES,
        max_length=256,
        verbose_name="Was an EMS coordinating centre (the centre responsible for dispatching and coordinating EMS units to the scene) available in the affected country/ies at the time of the incident?"
    )

    ems_common_dialing_number = fields.CharField(
        null=True,
        blank=True,
        choices=YES_NO_CHOICES,
        max_length=256,
        verbose_name="Is there one common dialling number for all Emergency Services (fire, police, EMS)?"
    )

    ems_directly_declared = fields.CharField(
        null=True,
        blank=True,
        max_length=256,
        choices=YES_NO_UKNOWN_CHOICES,
        verbose_name="Can a major incident be declared directly by the person receiving an alert at the EMS coordinating centre?"
    )

    # EMS staff background
    basic_life_support_non_ems = fields.BooleanField(
        default=False,
        verbose_name="Basic Life Support by non-EMS professional"
    )

    basic_life_support_non_ems = fields.BooleanField(
        default=False,
        verbose_name="Basic Life Support by EMS professional"
    )

    non_physician_advanced_live_support = fields.BooleanField(
        default=False,
        verbose_name="non-physician Advanced Life Support by EMS professional"
    )

    life_support_on_scene_by_physician = fields.BooleanField(
        default=False,
        verbose_name="Advanced Life Support by On-scene Physician"
    )

    other = fields.CharField(
        null=True, blank=True, max_length=256
    )

    voluntary_organisations_available = fields.CharField(
        null=True, blank=True, max_length=256,
        verbose_name="Please specify which voluntary organizations are available to assist the EMS service in a normal setting?"
    )

    trauma_network = fields.CharField(
        null=True, blank=True, max_length=256, choices=YES_NO_UKNOWN_CHOICES,
        verbose_name="Does the country where the major incident took place have a trauma network?"
    )

    regional_trauma_hospitals = fields.BooleanField(
        default=False,
        verbose_name="Are there any regional hospital/s with trauma specialty that exists within the EMS catchment system that was affected by the major incident?"
    )

    TRIAGE_SYSTEM_CHOICES = (
        ('Yes', 'Yes'),
        ('Yes, but different triage systems exist in different regions', 'Yes, but different triage systems exist in different regions',),
        ('No', 'No',),
        ('Unknown', 'Unknown',)
    )

    pre_hospital_triage_system = fields.CharField(
        blank=True, null=True, choices=TRIAGE_SYSTEM_CHOICES, max_length=256,
        verbose_name="Is a pre-hospital triage system in use on a daily basis on regional levels?"
    )

    TRIAGE_REGIONAL_CHOICES = (
        ("Yes", "Yes"),
        ("Yes, but different triage systems exist in different region", "Yes, but different triage systems exist in different region"),
        ('No', 'No',),
        ('Unknown', 'Unknown',)
    )

    pre_hospital_triage_regional = fields.CharField(
        blank=True, null=True, choices=TRIAGE_REGIONAL_CHOICES, max_length=256,
        verbose_name="Is a pre-hospital triage system in use for major incidents on regional levels?"
    )

    regional_response_plan_including_all_emergency_services = fields.CharField(
        blank=True, null=True, choices=YES_NO_UKNOWN_CHOICES, max_length=256,
        verbose_name="Is there a regional major incident response plan incorporating all emergency services within the area that the the major incident occured?"
    )
