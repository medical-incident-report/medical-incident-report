"""
mir models.
"""
from django.db.models import fields
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


class MainAuthor(models.PatientSubrecord):
    _is_singleton = True
    surname = fields.CharField(max_length=255, blank=True)
    first_name = fields.CharField(max_length=255, blank=True)
    title = ForeignKeyOrFreeText(models.Title)
    middle_name = fields.CharField(max_length=255, blank=True, null=True)
    email = fields.CharField(max_length=255, blank=True, null=True)
    role = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Please describe which role the author had in the major incident"
    )
    country = ForeignKeyOrFreeText(models.Destination)


class PreIncidentData(models.PatientSubrecord):
    country = ForeignKeyOrFreeText(models.Destination)
    more_than_one_country = fields.BooleanField(default=False)
    discription_area_of_the_incident = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Description of the area of the incident"
    )
    discription_the_special_circumstances = fields.TextField(
        blank=True,
        null=True,
        verbose_name="Description of the area of the incident"
    )


class RegisterIncident(models.PatientSubrecord):
    _is_singleton = True
    CASUALTIES_CHOICES = (
        ("0-10", "0-10",),
        ("11-20", "11-20",),
        ("21-30", "21-30",),
    )
    incident_name = fields.CharField(max_length=255, blank=True)
    link_to_the_newsfeed = fields.CharField(max_length=255, blank=True)
    number_of_casualties = fields.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=CASUALTIES_CHOICES
    )
    where_its_happend = fields.CharField(
        max_length=255, blank=True, null=True
    )
