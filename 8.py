preucola=int(input("cuant val el refresc de cola?\n*"))
colavenda=int(input("quina quantitat s'ha venut?\n*"))
preutaronja=int(input("cuant val la taronja?\n*"))
taronjavenda=int(input("quantitat de vendes\n*"))
preullimona=int(input("cuant val la llimona?\n*"))
llimonavenda=int(input("quantitat de vendes\n*"))
print("amb la taronjahas guanyat:", preutaronja*taronjavenda)
print("amb la llimona has guanyat:", preullimona*llimonavenda)
print("amb la cola has guanyat:", preucola*colavenda)
print("Total diners:",preucola*colavenda+preullimona*llimonavenda+preutaronja*taronjavenda)
