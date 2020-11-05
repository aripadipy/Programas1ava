print("""
  1)1
  2)2
  3)3
  4)4
  5)5
  6)6
  """)
dado=int(input("Que valor t'ha donat"))
if dado==5:
 print("Cinc i la seva cara oposada es 2")
elif dado==4:
 print("Quatre i la seva cara oposada es 3 ")
elif dado==3:
 print("Tres i la seva cara oposada es 4")
elif dado==1:
 print("UN i la seva cara oposada es 6")
elif dado==6:
 print("Sis i la seva cara oposada es 1")
elif dado==2:
 print("Dos i la seva cara oposada es 5")
else:
 print("El número introduït es erroni")