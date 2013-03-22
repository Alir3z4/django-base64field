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




class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
