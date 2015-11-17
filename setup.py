from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='tpic-webp',
      version=version,
      description="Webp to JPEG reverse proxy",
      long_description="""\
              Convert webp to jpeg for backward compatibility of some QQ clients against q*.tpic.cn
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Tydus',
      author_email='tydus@tydus.org',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "tornado>=3.0",
          "pillow>=2.6",
      ],
      entry_points={
          'console_scripts': [
              'tpicwebpd = tpicwebp.__main__:main',
          ]
      }
)
