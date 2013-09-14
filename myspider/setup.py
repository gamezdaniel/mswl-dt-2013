from setuptools import setup, find_packages

setup (name = 'My spider for web pages',
       version = '0.1',
       packages = find_packages (),
       scripts = ['myspider'],
       install_requires = ['bs4'],
       package_data = {},
       author = 'Testing',
       author_email = 'dgamez@localhost',
       description = 'description',
       license = '' ,
       keywords = '' ,
       url = '' ,
       long_description = '' ,
       download_url = '' ,
       )
