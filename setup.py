#!/usr/bin/env python
# coding: utf8

from __future__ import with_statement
from setuptools import setup, find_packages

import multiprocessing

setup(
    name='django-assets',
    version='0.7.3',
    url='http://github.com/miracle2k/django-assets',
    license='BSD',
    author='Michael Elsdörfer',
    author_email='michael@elsdoerfer.com',
    description='Asset management for Django, to compress and merge '\
                'CSS and Javascript files.',
    long_description=__doc__,
    packages = find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Django>=1.1',
        'webassets>=0.8',
        ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
    ],
)
