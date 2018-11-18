# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


setup(
    name='wp_honeypot',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Create a fake WordPress login page that logs email addresses and redirects bots to a 10gb download file.',
    long_description='For installation instructions see https://github.com/KalobTaulien/wp_honeypot',
    url='https://github.com/KalobTaulien/wp_honeypot',
    author='Kalob Taulien',
    author_email='kalob@kalob.io',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    install_requires=[
        'django-model-utils==3.0.*',
        'Django>=2.0'
    ]
)
