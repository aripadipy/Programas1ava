nombre1=int(input("Posa un nombre"))
nombre2=int(input("Posa un altre nombre"))
nombre3=int(input("Posa un nombre"))
if nombre1<=nombre2:
	if nombre2>=nombre3:
		if nombre3>=nombre1:print(nombre2,nombre3,nombre1)
		else:print(nombre2,nombre1,nombre3)
	else:print(nombre3,nombre2,nombre1)
else:
	if nombre1>=nombre3:
		if nombre3>=nombre2:print(nombre1,nombre3,nombre2)
		else:print(nombre1,nombre2,nombre3)
	else:print(nombre3,nombre1,nombre2)


