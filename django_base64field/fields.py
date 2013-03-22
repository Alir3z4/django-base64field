from django.db.models import signals
from django.db.models.fields import CharField

class Base64Field(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 255)
        kwargs['blank'] = kwargs.get('blank', True)
        kwargs['editable'] = kwargs.get('editable', False)
        kwargs['default']  = kwargs.get('default', '')
        kwargs['unique'] = True
        super(Base64Field, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(Base64Field, self).contribute_to_class(cls, name)
        cls._base64field_name = name
        signals.post_save.connect(self.generate_encoded_pk, cls)

    def generate_encoded_pk(self, sender, **kwargs):
        instance = kwargs['instance']
        field_name = instance._base64field_name

        if getattr(instance, field_name) in ['', None]:
            from django.utils.baseconv import base64

            obj_pk = instance.pk

            sender._default_manager.filter(pk=obj_pk).update(
                **{field_name:base64.encode(obj_pk)}
            )

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^django_base64field\.fields\.Base64Field"])
except ImportError:
    # No error should silently get passed my ASS!
    pass
