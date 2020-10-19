from math import sqrt
A=int(input("Escriu un nombre"))
B=int(input("Escriu un altre nombre"))
C=int(input("Escriu l'ultim nombre"))
if ((B**2)-4*A*C)<0:
	print("No hi ha solució")
else:
	x1=(-B+sqrt(B**2-(4*A*C))/2*A)
	x2=(-B-sqrt(B**2-(4*A*C))/2*A)
	print("Las solucions de l'ecuació són:")
	print(x1)
	print(x2)
