print("condicionales simples")
edad = input("Diga su edad:")
if (int(edad)>=18):
    print("Mayor de edad, permitido para viajar")

print("Cumple dos caminos")
temperatura=input("Incluye temperatura:")
if(int(temperatura)>=38):
    print("Temperatura alta, prohibido viajar")
else:
    print("Temperatura normal, permitido viajar")
    
    
print("condicionales multiples")
Preciodesupasaje=input("Incluir precio del pasaje:")
if(int(Preciodesupasaje)>=90):
    print("Clase ejecutiva")
elif (int(Preciodesupasaje)>=80):
    print("Clase turista")
elif (int(Preciodesupasaje)>=70):
    print("Clase económica")
else:
    print("Saldo insuficiente")
    
    
print("condicionales if anidados")
tiene_reserva=True
dinero=25
plato="pizza"
if(tiene_reserva):
    if(dinero>=20):
        if plato=="pizza":
            print("Tu pizza cuesta $20. Pedido confirmado")
        else:
            print("Plato disponible")
    else:
        print("Dinero insuficiente")
else:
    print("No tiene reserva")
    