from setuptools import setup, find_packages

setup (name = 'webcrawler',
       version = '0.1',
       packages = find_packages (),
       scripts = ['webcrawler'],
       install_requires = ['bs4'],
       package_data = {},
       author = 'Daniel Gamez',
       author_email = 'd.gamez@alumnos.urjc.es',
       description = 'Web Crawler',
       license = 'BSD 2-clause' ,
       keywords = 'web crawler spider' ,
       url = '' ,
       long_description = 'Web Crawler' ,
       download_url = '' ,
       )
