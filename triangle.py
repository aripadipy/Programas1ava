cos1=int(input("Costat 1\n"))
cos2=int(input("Costat 2\n"))
cos3=int(input("Costat 3\n"))
if cos1>cos2+cos3:
  print("Es un triangle")
elif cos1+cos2<cos3:
  print("Es un triangle")
elif cos1+cos3<cos2:
  print("Es un triangle")
else:
  print("No es un triangle")
