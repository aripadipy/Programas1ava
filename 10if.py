import calendar
dia=int(input("Dime un dia\n"))
mes=int(input("Dime un mes\n "))
año=int(input("Dime un año\n"))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia>=1 and dia<=31 and año>=1:
	print("1Correcte")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia>=1 and dia<=30 and año>=1:
	print("2correcte")
elif calendar.isleap(año) and mes==2 and dia>=1 and dia<=29 and año>=1:
  print("la data es correcta")
elif not calendar.isleap(año) and mes==2 and dia>=1 and dia<=28 and año>=1:
  print ("correcte")
else:
  print("La data es incorrecta")