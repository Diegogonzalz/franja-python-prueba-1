print("Escoger tipo de cambio:","Pesos Mexicanos a U$: escribir 1","Pesos Chilenos a U$ escribir 2" ,"Pesos Argentinos a U$escribir 3")
pregunta_1=int(input("tipo:"))

pregunta_2=float(input("Cantidad a cambiar: "))

precio_mex_dolar=20 
precio_chile_dolar=855
precio_arg_dolar=115
    
if pregunta_1== 1:
    pm=pregunta_2/precio_mex_dolar
    pm=str(pm)
    print("Son "+pm+" U$")
elif pregunta_1==2:
    pc=pregunta_2/precio_chile_dolar
    pc=str(pc)
    print("Son "+pc+" U$") 
else:
    pa=pregunta_2/precio_arg_dolar
    pa=str(round(pa,2))
    print("Son "+pa+" U$") 

