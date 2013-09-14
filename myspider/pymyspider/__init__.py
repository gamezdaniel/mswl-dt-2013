# Info Licencia

import urllib2
from bs4 import BeautifulSoup as Soup

def retrieve_url (url):
  
  opener = urllib2.build_opener ()
  try:
    t = opener.open (url).read ()
    parser = Soup(t)
    return [x['href'] for x in parser.findAll('a') if x.has_attr('href')]
    
  except urllib2.URLError:
    return []
