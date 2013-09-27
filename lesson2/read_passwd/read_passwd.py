'''
Created on Sep 27, 2013
Testing
@author: dgamez
'''

def run():
    t = lee_passwd ()
  
    for l in t:
        # print l
        e = l.split(":")
        user = e[0]
        shell = e[-1].rstrip("\n")
        print "%s -> %s" % (user, shell)
    
  
def lee_passwd ():
    f = open('/etc/passwd','r')
    t = f.readlines ()
    f.close ()
  
    return t

if __name__ == '__main__':
    run ()