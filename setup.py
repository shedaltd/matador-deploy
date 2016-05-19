"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join

from setuptools import Command, find_packages, setup

from app import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'ganado-deploy',
    version = __version__,
    description = 'A Rancher Deployment CLI App',
    long_description = long_description,
    url = 'https://github.com/seedtech/rancher-deploy',
    author = 'Timon Sotiropoulos',
    author_email = 'timon@seeddigital.co',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'ganado-deploy=app.main:main',
        ],
    },
)
