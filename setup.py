#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Philip Abbet <philip.abbet@idiap.ch>

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.extension']))

from bob.extension.utils import load_requirements
install_requires = load_requirements()

# Define package version
version = open("version.txt").read().rstrip()

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='bob.db.put_vein',
    version=version,
    description='PUT Vein Database Access API for Bob',
    url='http://pypi.python.org/pypi/xbob.db.putvein',
    license='GPLv3',
    author='Philip Abbet',
    author_email='philip.abbet@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,


    install_requires = install_requires,

    entry_points={

      # declare the database to bob
      'bob.db': [
        'putvein = bob.db.putvein.driver:Interface',
      ],
    },

    classifiers = [
      'Framework :: Bob',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
    ],

)
