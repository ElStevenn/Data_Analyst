#!/usr/bin/env python

from setuptools import setup, find_packages
import sys
import os

def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    file = open(filepath, 'r')
    return file.read()



setup(
    name='Data Analyst',
    version='1.0.0',
    author='Pau Mateu Esteve',
    author_email='paumat17@gmail.com',
    description='These are a sort scripts and where I learn data analyst',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license='GNU General Public License v3.0',
    keywords=['Pandas',
              'Numpy',
              'Jupyter',
              'Notebooks',
              'Data Cleaning',
              'Data Frames'],
    url='https://www.instagram.com/sstevenn123_/',
    packages=find_packages(),
    scripts=[],
    install_requires=['pandas','numpy','requests'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
)


sys.exit()