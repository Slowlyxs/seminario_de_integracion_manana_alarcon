print("condicionales simples")
edad = input("Incluye edad?")
if (int(edad)>=18):
    print("Mayor de edad")
    

print("Cumple dos caminos")
temperatura=input("Incluye temperatura:")
if(int(temperatura)>=38):
    print("Temperatura alta")
else:
    print("Temperatura normal")
    
    
print("condicionales multiples")
nota=input("Incluir nota:")
if(int(nota)>=90):
    print("Excelente")
elif (int(nota)>=80):
    print("Bueno")
elif (int(nota)>=70):
    print("Aprobado")
else:
    print("Reprobado")
    
    
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
    
    

print("Participacion")
tiempo_antiguedad= input("Indique sus años de antiguedad:")
calificacion_desempeño=input("Calificacion de desempeño laboral:")
salario=input("Ingrese su salario")
if(int(tiempo_antiguedad) > 1):
    if(int(calificacion_desempeño)>=8)                                                                                                                                                                                                                                                                                                                              :
        print("Puede optar a un bono")
        if(int(salario)<1000):
            print("BONO DE 200")
        else:
            print("bono de 100")
    else:
        print("No recibe bono")
else:
    print("No cumple el año")