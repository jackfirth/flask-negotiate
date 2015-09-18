"""
flask-negotiate2
===============

Content negotiation utility for Flask apps. Fork of Flask-Negotiate by
Matt Wright (github.com/mattupstate)


Resources
---------

- `Documentation <http://packages.python.org/flask-negotiate2/>`_
- `Issue Tracker <http://github.com/jackfirth/flask-negotiate/issues>`_
- `Code <http://github.com/jackfirth/flask-negotiate/>`_

"""
from setuptools import setup

setup(
    name='flask-negotiate2',
    version='0.2.0',
    url='https://github.com/jackfirth/flask-negotiate',
    license='MIT',
    author='Matthew Wright',
    author_email='matt@nobien.net',
    description='Content negotiation utility for Flask apps',
    long_description=__doc__,
    py_modules=['flask_negotiate2'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['flask'],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
