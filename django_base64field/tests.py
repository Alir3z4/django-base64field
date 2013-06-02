from django.test import TestCase
from django.utils.baseconv import base64
from django_base64field.tests.models import Planet, Continent, Helper


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
        self.assertNotEqual(planet.ek, same_planet_but_fresh.ek)

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
        finally:
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

    def test_field_with_helper_defined(self):
        """
         Look at `Helper` Model. Won't be any headache for retrieving the
        object after creation from database anymore.
        """
        hell = Helper.objects.create()

        #  On `hell` instance there is no `ek` available
        # because It will be available on the next retrieving of `Helper`
        self.assertIn(hell.ek, ['', None])
        self.assertNotEqual(hell.ek, hell._ek())

        #  But if `ek` is need it immediately for any reason
        # `ek` will be available on `_ek()` method.
        # Without any refreshing/retrieving `hell` instance again
        # from database
        self.assertIsNotNone(hell._ek())
        self.assertNotIn(hell._ek(), ['', None])

