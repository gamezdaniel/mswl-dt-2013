# Copyright (c) 2013, Daniel Gamez
# All rights reserved.
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
# 1) Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 2) Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer 
#    in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, 
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import sys

def run():
  
  argc = len (sys.argv)
  
  if argc == 1:
    print "Escribe el nombre de usuario!"
    # sys.exit (2)
    return
  
  user = sys.argv[1]
  # Comentarios
  passwd = lee_passwd ()

  if user in passwd.keys ():
    print "%s -> %s" % (user, passwd[user])    
  else:
    print "El usuario %s no existe!" % user
    
  
def lee_passwd ():
  f = open('/etc/passwd','r')
  t = f.readlines ()
  f.close ()
  
  # empty dictionary
  d = {}
  
  for l in t:
    # print l
    e = l.split(":")
    user = e[0]
    shell = e[-1].rstrip("\n")
    d[user] = shell
    
    # print "%s -> %s" % (user, shell)
  return d
    
if __name__ == '__main__':
  run ()
  