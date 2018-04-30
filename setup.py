#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

try:
    long_description = open('README.md').read()
except:
    long_description = ''

setup(
    name='python-nessus',
    version="0.2.0",
    description='A wrapper around the tapioca-nessus for translating the'
                ' Nessus API documents into Python Objects',
    long_description=long_description,
    author="Flávio Cardoso Ferreira Pontes",
    author_email="flavio.pontes@siteblindado.com.br",
    url='https://github.com/siteblindado/nessus-report-parser',
    packages=[
        'nessus',
    ],
    python_requires='>=3.3',
    package_dir={'nessus': 'nessus'},
    package_data={
        '': ['LICENSE.txt', 'README.rst', '*.json']
    },
    include_package_data=True,
    install_requires=[
        'tapioca-nessus',
        'lxml'
    ],
    license="MIT",
    zip_safe=False,
    keywords='nessus',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=['pytest']
)
