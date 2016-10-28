from django.db import models


class University(models.Model):
    name = models.TextField()
    professors = models.IntegerField(blank=True, null=True)
    students = models.IntegerField(blank=True, null=True)
    doctors = models.IntegerField(blank=True, null=True)


class Direction(models.Model):
    code = models.CharField(max_length=20)
    name = models.TextField()
    bachelor = models.ForeignKey(University)
    master = models.ForeignKey(University)
    specialist = models.ForeignKey(University)


class Rating(models.Model):
    university = models.ForeignKey(University)
    min_rating = models.IntegerField()
    max_rating = models.IntegerField()
    type = models.CharField(choices=(('national', 'national'), ('international', 'international')))


class Stats(models.Model):
    year = models.IntegerField()

