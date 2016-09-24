# -*- coding: utf-8 -*-
"""Installer for the collective.sandboxlib package."""

from setuptools import find_packages
from setuptools import setup


# long_description = (
#     open('README.md').read()
#     + '\n' +
#     'Contributors\n'
#     '============\n'
#     + '\n' +
#     open('CONTRIBUTORS.rst').read()
#     + '\n' +
#     open('CHANGES.rst').read()
#     + '\n')


setup(
    name='plonecensus',
    version='0.1',
    description="Plone plugin to collect stats about plugin usage",
#    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.6",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='PretaGov',
    author_email='software@pretaweb.com',
    url='http://pypi.python.org/pypi/falling',
    license='GPL',
    packages=find_packages('.', exclude=['ez_setup']),
    package_dir={'': '.'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'rapido.plone'
    ],
    extras_require={
        'test': [
#            'plone.app.testing',
#            'plone.app.contenttypes',
#            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
