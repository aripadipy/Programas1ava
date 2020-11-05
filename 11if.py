import calendar
dia=int(input("Dime un dia\n"))
mes=int(input("Dime un mes\n "))
año=int(input("Dime un año\n"))
hora=int(input("Dime una hora"))
minutos=int(input("Dime los minutos"))
segundos=int(input("Dime los segundos"))
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia>=1 and dia<=31 and año>=1 and hora>=1 and hora<=24 and minutos>=1 and minutos<=60 and segundos>=1 and segundos<=60:
 print("Correcte")
 if segundos == 59 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24:
   print(dia,mes,año,hora,minutos+1,segundos*0) 
 elif segundos<=58 and segundos>0 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
  print(dia, mes, año, hora, minutos, segundos+1)
 elif segundos==59 and minutos==59 and hora == 23 and dia<31: 
  print(dia+1, mes, año, hora*0, minutos*0, segundos*0)
 elif segundos==59 and minutos==59 and hora<= 22: 
  print(dia, mes, año, hora+1, minutos*0, segundos*0)
 elif segundos==59 and minutos==59 and hora== 23 and dia==31 and mes<=11: 
  print(dia-30, mes+1, año, hora*0, minutos*0, segundos*0)
 elif segundos==59 and minutos==59 and hora== 23 and dia==31 and mes==12: 
  print(dia-30, mes-11, año+1, hora*0, minutos*0, segundos*0)
 else:
  print("INcorrecte")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia>=1 and dia<=30 and año>=1 and hora>=1 and hora<=24 and minutos>=1 and minutos<=60 and segundos>=1 and segundos<=60:
 print("correcte")
 if segundos == 59 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
  print(dia,mes,año,hora,minutos+1,segundos*0) 
 elif segundos<=58 and segundos>0 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
  print(dia, mes, año, hora, minutos, segundos+1)
 elif segundos==59 and minutos==59 and hora <= 23 and dia<30: 
  print(dia+1, mes, año, hora*0, minutos*0, segundos*0)
 elif segundos==59 and minutos==59 and hora== 22: 
   print(dia, mes, año, hora+1, minutos*0, segundos*0)
 elif segundos==59 and minutos==59 and hora== 23 and dia==30 and mes<=11: 
   print(dia-29, mes+1, año, hora*0, minutos*0, segundos*0)
 else:
   print("incorrecte")
elif calendar.isleap(año) and mes==2 and dia>=1 and dia<=29 and año>=1 and hora>=1 and hora<=24 and minutos>=1 and minutos<=60 and segundos>=1 and segundos<=60:
  print("la data es correcta")
if segundos == 59 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
  print(dia,mes,año,hora,minutos+1,segundos*0) 
elif segundos<=58 and segundos>0 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
 print(dia, mes, año, hora, minutos, segundos+1)
elif segundos==59 and minutos==59 and hora >0 and hora <= 22 and dia<29: 
 print(dia+1, mes, año, hora*0, minutos*0, segundos*0)
elif segundos==59 and minutos==59 and hora== 23: 
 print(dia, mes, año, hora+1, minutos*0, segundos*0)
elif segundos==59 and minutos==59 and hora== 23 and dia==29 and mes<=11: 
 print(dia-28, mes+1, año, hora*0, minutos*0, segundos*0)
elif segundos==59 and minutos==59 and hora== 23 and dia==29: 
 print(dia-28, mes-11, año+1, hora*0, minutos*0, segundos*0)
elif not calendar.isleap(año) and mes==2 and dia>=1 and dia<=28 and año>=1and hora>=1 and hora<=24 and minutos>=1 and minutos<=60 and segundos>=1 and segundos<=60:
  print ("correcte")
if segundos == 59 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
 print(dia,mes,año,hora,minutos+1,segundos*0) 
elif segundos<=58 and segundos>0 and minutos >0 and minutos <= 58 and hora >0 and hora <= 24: 
 print(dia, mes, año, hora, minutos, segundos+1)
elif segundos==59 and minutos==59 and hora >0 and hora <= 22 and dia<28: 
 print(dia+1, mes, año, hora*0, minutos*0, segundos*0)
elif segundos==59 and minutos==59 and hora== 23: 
 print(dia, mes, año, hora+1, minutos*0, segundos*0)
elif segundos==59 and minutos==59 and hora== 23 and dia==28 and mes<=11: 
 print(dia-27, mes+1, año, hora*0, minutos*0, segundos*0)
elif segundos==59 and minutos==59 and hora== 23 and dia==28: 
 print(dia-27, mes-11, año+1, hora*0, minutos*0, segundos*0)
else:
  print("La data es incorrecta")
