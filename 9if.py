dia=int(input("Dime un dia en numero"))
mes=int(input("Dime un mes en numero"))
año=int(input("Dime un año"))
if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia>=1 or dia<=31 and any<=2020:
	print("Correcte")
elif (mes==4 or mes==6 or mes==9) and dia>=1 and dia<=30:
	print("correcte")
elif (mes==2) and dia<=28:
	print("Correcte")
else:
  print("La data es Incorrecte")