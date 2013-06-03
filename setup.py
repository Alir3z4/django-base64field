from distutils.core import setup

setup(
    name='django-base64field',
    version='1.0',
    packages=['django_base64field'],
    url='https://github.com/Alir3z4/django-base64field',
    license=open('LICENSE').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    install_requires=['django', ],
    description='A motherfucking django model field to bring base64 encoded'
                ' key to models.',
    long_description=open('README.rst').read(),
    keywords=[
        'django',
        'base64',
        'field'
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development'
    ],

)
