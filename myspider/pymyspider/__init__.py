# Copyright (c) 2013, Daniel Gamez
# with the help of Israel Herraiz at URJC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
# 1) Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
# 
# 2) Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation 
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.
#

import urllib2
from bs4 import BeautifulSoup as Soup
from urlparse import urlparse, urljoin


### URL's Retriever

def retrieve_links (url):
  """This function retrieve links from the URL provided
  The URL must be in any of these formats:
  http://
  """
  opener = urllib2.build_opener ()
  
  try:
    t = opener.open (url).read ()
    parser = Soup(t)
    return [x['href'] for x in parser.findAll('a') if x.has_attr('href')]

  except urllib2.URLError:
    return []
    

### Obtain links list by depth per URL
def links_list (url, depth):

  # Base case
  if depth == 0:

    l = retrieve_links (url)
    
    for each in l:
      print " - %s" % each
      
    return l
    
  else:
    # Get URL base on b
    b = validate_url (url)

    #if not b:
      #return "Invalid URL"
    
    l = retrieve_links (url)
    
    for each in l:
      
      # Get URL base on e
      e = validate_url (each)
      
      # Correct list url item
      if not e:
	l[l.index(each)] = urljoin(b, each)

    for each in l:
      print " %s %s" % ("*"*depth, each)
      l2 = links_list (each, depth-1)

  print ""

  
### URL Validator
    
def validate_url (url):
  v = urlparse(url)
  
  if v.scheme and v.hostname:
    # Get URL base and hostname to form correct URL base
    u = v.scheme + '://' + v.hostname + '/'
    return u
  else:
    # Not a valid URL
    return False
    
