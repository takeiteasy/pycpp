#!/usr/bin/env python

from setuptools import setup, find_packages
import os, pycpp

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()
    
setup(
    name='pycpp',
    version=pycpp.version,
    description='A C11 preprocessor written in pure Python',
    long_description=long_description,
    author='George Watson, Niall Douglas, and David Beazley',
    url='https://github.com/takeiteasy/pycpp',
    packages=['pycpp', 'pycpp/ply/ply'],
    package_data={'pycpp' : ['LICENSE']},
    test_suite='tests',
    entry_points={
        'console_scripts': [ 'pycpp=pycpp:main' ]
    },
    options={'bdist_wheel':{'universal':True}},
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
