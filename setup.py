# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def parse_requirements_file(file_path):
    lines = []
    with open(file_path) as f:
        for line in f:
            line = line.partition('#')[0]
            line = line.rstrip()
            if line:
                lines.append(line)
    return lines


requires = parse_requirements_file('requirements.txt')


setup(
    name='slowpoke',
    version='0.1',
    description='',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Andrew Zhu',
    author_email='dir01@dir01.org',
    url='',
    keywords='wsgi proxy delay',
    packages=find_packages(),
    install_requires=requires,
)
