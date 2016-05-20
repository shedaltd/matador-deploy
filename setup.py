"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from setuptools import Command, find_packages, setup
from app import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'matador-deploy',
    version = __version__,
    description = 'A Bullish Rancher Deployment CLI App',
    long_description = long_description,
    url = 'https://github.com/seedtech/matador-deploy',
    download_url = 'https://github.com/seedtech/matador-deploy/archive/0.4.tar.gz',
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
    packages = find_packages(),
    install_requires = [
        "cattle==0.5.4",
        "rainbow_logging_handler==2.2.2"
    ],
    entry_points = {
        'console_scripts': [
            'matador-deploy=app.main:main',
        ],
    },
)
