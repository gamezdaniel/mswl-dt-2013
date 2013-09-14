import sys

def run():
  
  argc = len (sys.argv)
  
  if argc != 4:
    print "Muy pocos argumentos!"
    # sys.exit (2)
    return

  op1 = float(sys.argv[1])
  op  = sys.argv[2]
  op2 = float(sys.argv[3])

  if op == '+':
    print op1 + op2
    
  elif op == '-':
    print op1 - op2
    
  elif op == '*':
    print op1 * op2
    
  elif op == '/':
    print op1 / op2
    
  else:
    print "Operacion No Permitida!"
    
if __name__ == '__main__':
  run ()
