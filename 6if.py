var1=int(input("Preu original"))
var2=int(input("Preu pagat"))
var3=input("Vols saber el descompte?")
descompteporcentaje=float(100*var2)/var1
if var3=="si":print("Has pagat un:",descompteporcentaje)
