from setuptools import setup, find_packages
import os

version = '3.1'

setup(name='teamrubber.viewletesi',
      version=version,
      description="",
      long_description=open(os.path.join('src', 'teamrubber', 'viewletesi', 'README.txt')).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      package_dir = {'':'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['teamrubber'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.testcaselayer',
          'chameleon.zpt',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.filter_factory]
      esi = teamrubber.viewletesi.middleware:ESIMiddlewareFactory
      """,
      )
