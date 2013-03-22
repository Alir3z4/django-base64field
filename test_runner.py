import os
import sys
from django.conf import settings

DIR_NAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=(
        'django_base64field',
    )
)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)

failures = test_runner.run_tests(['django_base64field', ])

if failures:
    sys.exit(failures)
