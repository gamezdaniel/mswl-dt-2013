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
  