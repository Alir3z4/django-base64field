from django.db import models
from django.test import TestCase
from django.utils.baseconv import base64
from django_base64field.fields import Base64Field

class Planet(models.Model):
    ek = Base64Field()
    name = models.CharField(
        default='Fucker',
        max_length=103
    )


class Continent(models.Model):
    ek = Base64Field()
    name = models.CharField(
        default='Suckers!',
        max_length=13
    )
    planet = models.ForeignKey(Planet, to_field='ek')


class TestBase64Field(TestCase):

    def test_field_is_none_after_creation(self):
        planet = Planet.objects.create(name='Fucking Earth')

        self.assertIn(planet.ek, ['', None])
        self.assertIsNotNone(planet.pk)

    def test_field_not_none_after_saved(self):
        planet = Planet.objects.create(name='Little Planet')
        base64_key = base64.encode(planet.pk)
        saved_planet = Planet.objects.get(pk=planet.pk)

        self.assertEqual(saved_planet.ek, base64_key)





