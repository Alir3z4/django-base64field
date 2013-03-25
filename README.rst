==================
Django Base64Field
==================

.. contents:: Table of contents

Overview
--------

- A motherfucking django model field to bring ``base64`` encoded key to models.
- It uses ``base64`` from ``django.utils.baseconv`` for encoding.

How it works?
--------------

You just define a field on your model as ``Base64Field()``
::

    from django_base64field.fields import Base64Field
    
    class Planet(models.Model):
        ek = Base64Field()


Each time new ``Planet`` saved, A *base64* encoded key based on ``Planet`` 
Primary Key will generated and set to ``ek``. This is happens just one 
fucking time, Exactly after new ``Planet`` created and successfully inserted
into Database, But the next billions times when ``Planet``  updated or saved
``ek`` won't get touched.

You wanna know more about how ``django-base64field`` works? Then get da fuck
out of ``README.rst`` and go look inside ``django_base64field.tests.py``.

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

Then install it by running:
::

    $ python setup.py install
