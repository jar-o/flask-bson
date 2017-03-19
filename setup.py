"""
Flask-BSON
-------------

Allow your flask endpoints to speak BSON.
"""
from setuptools import setup

setup(
    name='Flask-BSON',
    version='0.1.1',
    url='http://www.github.com/jar-o/flask-bson/',
    license='MIT',
    author='James Robson',
    author_email='flask-bson@googlegroups.com',
    description='Let your flask endpoints handle BSON requests and responses',
    long_description=__doc__,
    py_modules=['flask_bson'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'bson'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_bson'
)
