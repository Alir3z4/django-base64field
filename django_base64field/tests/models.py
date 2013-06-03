from django.db import models
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


class Helper(models.Model):
    """
    base64 encoded value won't be available at first time creation.
    It can ve accessible by getting the object from database after creation
    mean when it get saved completely, But what if we don't want to get our base64
    encoded key from our sweet model by retrieving it again from database?

    It's easy, efficient, holly and molly!
    """
    ek = Base64Field()

    def _ek(self):
        if self.ek: return self.ek

        if not self.ek and self.pk:
            return base64.encode(self.pk)

        return self.ek


class CustomReceiver(models.Model):
    """
    Passing custom receiver to generate `youyouid` with a custom receiver.
    """
    youyouid = Base64Field(
        encode_receiver='django_base64field.tests.receivers:custom_receiver'
    )

