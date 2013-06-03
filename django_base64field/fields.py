import importlib
from django.db.models import signals
from django.db.models.fields import CharField


class Base64Field(CharField):
    """
     Base64Field is useful where you need a base64 encoded value from
    model's Primary Key a.k.a PK which is available on every django
    application model by default. Sine `base64` encoder works with
    `integer` value then PK should be also `integer`, Fortunately
    again `PK` field is `integer` by nature.

     When a model get saved, `post_save` signal will be emitted,
    This is where a base64 encoded key will be generated/encoded
    from model's `PK`, Then model will get **updated** not saved again.
    this operation happens just one the first time model get saved.
    In next time model get saved or updated `base64` won't get generated.

    Usage
    -----
    >>> from django.db import models
    >>> from django_base64field.fields import Base64Field
    >>>
    >>> class MyModelianto(models.Model):
    >>>     ek = Base64Field()
    >>>
    >>> modelia = MyModelianto.objects.create(pk=314159265358979323)
    >>> modelia.ek
    >>> u''
    >>> refreshed_modelia = MyModelianto.objects.get(pk=modelia.pk)
    >>> refreshed_modelia.ek
    >>> u'HS7Y_sdg3x'
    """

    def __init__(self, encode_receiver=None, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 255)
        kwargs['null'] = kwargs.get('null', True)
        kwargs['blank'] = kwargs.get('blank', True)
        kwargs['default'] = kwargs.get('default', '')
        self.encode_receiver = encode_receiver
        super(Base64Field, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(Base64Field, self).contribute_to_class(cls, name)
        cls._base64field_name = name
        encode_receiver = self.generate_encoded_pk

        if self.encode_receiver:
            e_module, e_method = self.encode_receiver.split(':')
            e_module = importlib.import_module(e_module)
            encode_receiver = getattr(e_module, e_method)

        signals.post_save.connect(encode_receiver, cls)

    def generate_encoded_pk(self, sender, **kwargs):
        instance = kwargs['instance']
        field_name = instance._base64field_name

        if getattr(instance, field_name) in ['', None]:
            from django.utils.baseconv import base64

            obj_pk = instance.pk

            sender._default_manager.filter(pk=obj_pk).update(
                **{field_name: base64.encode(obj_pk)}
            )


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^django_base64field\.fields\.Base64Field"])
except ImportError:
    # No error should silently get passed my ASS!
    pass
