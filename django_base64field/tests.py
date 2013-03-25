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

    def test_field_is_none_on_creation(self):
        """
         After Planet has created, `planet.ek` won't be available.
        because `planet.ek` will be generated after `planet` has been saved.
        """
        planet = Planet.objects.create()

        self.assertIn(planet.ek, ['', None])
        self.assertIsNotNone(planet.pk)

    def test_field_not_none_after_saved(self):
        """
         After `Planet` has been created, `Planet.ek` will be available
        on next time of getting `planet` from database.

        Why?
        ----
             Because after `planet` get created, `post_save` signal of `Planet` will
            emitted, This is where `ek` field will be set from ``base64``
            encoded value based on `pk`.
        """
        planet = Planet.objects.create()
        base64_key = base64.encode(planet.pk)
        same_planet_but_fresh = Planet.objects.get(pk=planet.pk)

        self.assertEqual(same_planet_but_fresh.ek, base64_key)
        self.assertNotEquals(planet.ek, same_planet_but_fresh.ek)

    def test_field_for_fk_none_on_creation(self):
        """
         I just created a `Planet`, As you already know, `planet.ek` is not
        available on `planet` at the moment. It will be available on next
        retrieving from database. So `planet` can't be assigned for creating
        new `Continent` as FK on `Continent.planet`.
        """
        planet = Planet.objects.create()

        continent = None

        try:
            continent = Continent.objects.create(planet=planet)
        except:
            pass

        self.assertIsNone(continent)

    def test_field_for_fk_not_none_after_creation(self):
        """
         So I want to create new `Continent` for my new shiny funky punky ass
        `Planet` that I've just created, It's easy, just retrieving new
        planet from database to make `ek` available for it, Then it will be
        fucking freaking ok to assign the fresh `Planet` to
        our sucker `Continent`.
        """
        planet = Planet.objects.create()
        same_planet_but_fresh = Planet.objects.get(pk=planet.pk)
        continent = Continent.objects.create(planet=same_planet_but_fresh)

        self.assertIsNotNone(continent)
        self.assertIsInstance(continent, Continent)
        self.assertIn(continent.ek, ['', None])

        continent_pk = continent.pk
        same_continent_but_fresh = Continent.objects.get(pk=continent_pk)


        self.assertNotEqual(same_continent_but_fresh.ek, continent.ek)
        self.assertEqual(same_continent_but_fresh.ek, base64.encode(continent_pk))







