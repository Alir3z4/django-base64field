import uuid


def custom_receiver(sender, **kwargs):
    """
    Set `youyouid` field with custom uuid.uuid4() ;)
    """
    instance = kwargs['instance']
    field_name = instance._base64field_name

    if getattr(instance, field_name) in ['', None]:
        gen_uuid = str(uuid.uuid4())

        sender._default_manager.filter(pk=instance.pk).update(
            **{field_name: gen_uuid}
        )
