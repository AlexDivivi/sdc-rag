#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    file_path = join(dirname(__file__), *names)
    with io.open(file_path, encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='sdc-rag-backend',
    version='0.1',
    license='MIT',
    description='sdc-rag-backend',
    long_description=read('../README.md'),
    author='Alex Divivi',
    author_email=' ',
    url=' ',
    packages=find_packages('app'),
    package_dir={'': 'app'},
    zip_safe=False,
)