import random
n=int(input("Posa un numero del 0 al 10:\n"))
if n>=0 and n<=10:
  m=print("Crec que el teu numero es:",random.randint(0,10))
  if n==m:
    print("T'he llegit la ment")
  else:
    print("Torna a probar")
else:
  print("El numero ha de ser de 0 a 10")
  



