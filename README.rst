==================
Django Base64Field
==================

.. image:: https://travis-ci.org/Alir3z4/django-base64field.png
   :alt: travis-cli tests status for django-base64field
   :target: https://travis-ci.org/Alir3z4/django-base64field

.. contents:: Table of contents

Overview
--------

- A motherfucking django model field to bring ``base64`` encoded key to models.
- It uses ``base64`` from ``django.utils.baseconv`` for encoding.
- Tested on Python2.7, Python3.3 .

How it works?
--------------

``Base64Field`` is useful where you need a base64 encoded value from
model's Primary Key a.k.a PK which is available on every django
application model by default. Sine `base64` encoder works with
`integer` value then PK should be also `integer`, Fortunately
again `PK` field is `integer` by nature.

When a model get saved, `post_save` signal will be emitted,
This is where a base64 encoded key will be generated/encoded
from model's `PK`, Then model will get **updated** not saved again.
this operation happens just one the first time model get saved.
In next time model get saved or updated `base64` won't get generated.

You wanna know more about how ``django-base64field`` works? Then get da fuck
out of ``README.rst`` and go look inside ``django_base64field.tests.py``.

Usage
-----

Here is simple usage of ``Base64Field``
::
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
    >>> modelia.ek
    >>> u'HS7Y_sdg3x'

As You can see ``ek`` in not available on returned instance
from ``MyModelianto.objects.create()``, It will be available after retrieving
``refreshed_modelia`` from database which is same record as ``modelia`` here.

This behavior can be easily controlled with implementing a simple helper
method on ``MyModelianto``. You can find out more about this solution on
``django_base64field.tests.py``, Which it doesn't require to retrieving 
the instance from database after first creation just for getting ``ek` field.

Installation
------------
``django-base64field`` is available on pypi

http://pypi.python.org/pypi/django-base64field

So easily install it by ``pip``
::

    $ pip install django-base64field

Or by ``easy_install``
::

    $ easy_install django-base64field

Another way is by cloning ``django-base64field``'s
`git repo <https://github.com/Alir3z4/django-base64field>`_ ::

    $ git clone git://github.com/Alir3z4/django-base64field.git

Then install it by running
::

    $ python setup.py install

Or I don't know, Install it directly from git.
::

    pip install git+https://github.com/Alir3z4/django-base64field.git#egg=django-base64field


Some pkg have no installation method, This is awefuckingsome that
``django-base64field`` gives you many ways for installation.
