from django.db import models
from django.test import TestCase
from django.utils.baseconv import base64
from django_base64field.fields import Base64Field

class Planet(models.Model):
    ek = Base64Field()
    name = models.CharField(max_length=13)


class Continent(models.Model):
    ek = Base64Field()
    name = models.CharField(max_length=13)
    planet = models.ForeignKey(Planet, to_field='ek')


class TestBase64Field(TestCase):

    def test_field_is_none_after_creation(self):
        planet = Planet.objects.create(name='Fucking Earth')

        self.assertIn(planet.ek, ['', None])
        self.assertIsNotNone(planet.pk)


