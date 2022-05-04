#preguntar cantidad a invertir
#interes %anual
#num de años
#capital invertido obtenido en la inversion
#2 decimales
cantidad_invertir=float(input("Cantidad a invertir (U$): "))
interes_anual=float(input("Interes anual (%): " ))
num_años=int(input("Cantidad de años a invertir: "))
capital_ob=((cantidad_invertir*(((interes_anual/100)+1))**num_años))
capital_ob=round(capital_ob,2)
capital_ob=str(capital_ob)
print("Capital esperado (total): "+capital_ob+" U$")
