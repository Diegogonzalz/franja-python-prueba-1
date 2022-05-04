#barra de pan -->3.49 Euros
#pan no del dia 60% de descuento
#lea nu de barras numero bararras vendidas tipo "no del dia"
#mostrar precio habitual de un pan
#precio por no ser fresca y coste total

num_barras_no=int(input("escribe el numero de barras con rebaja: "))
precio_normal=3.49
total_precio_normal=(num_barras_no*precio_normal)
precio_normal=str(precio_normal)
print("El precio sin descuento es: "+precio_normal+" €")
descuento=60
precio_normal=float(precio_normal)
descuento_aplicado=round(((descuento*precio_normal)/100),2)
descuento_aplicado=str(descuento_aplicado)
print("descuento aplicado: "+descuento_aplicado+" €")
descuento_aplicado=float(descuento_aplicado)
total_pagar=round(num_barras_no*descuento_aplicado,2)
total_pagar=str(total_pagar)
print("total a pagar: "+total_pagar+" €")