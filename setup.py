
import os
import sys
from setuptools import setup

try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname

here = os.path.abspath(dirname(__file__))

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

setup(
    name='diffbot_api',
    version='0.1.0',
    description='Diffbot API Client.',
    long_description='See README.md file.',
    author='Colin Ricardo',
    author_email='me@colinricardo.com',
    url='https://github.com/colinricardo/diffbot_api',
    py_modules=['article_parser'],
    install_requires=['requests'],
    license='MIT',
    classifiers=(

    ),
)
