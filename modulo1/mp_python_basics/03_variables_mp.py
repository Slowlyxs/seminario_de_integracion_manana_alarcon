# Enteros, Cadena de caracteres, booleano, None
nombre_pasajero = "Alejandro Alarcon"         #String
edad_pasajero = 22                            #Entero
altura_pasajero = 1.72                        #float
activo_pasajero = True                        #booleano
nulo_pasajero = None                          #NoneType


print(type(nombre_pasajero))
print(type(edad_pasajero))
print(type(altura_pasajero))
print(type(activo_pasajero))
print(type(nulo_pasajero))

a,b,c =12,13,14
print(a)
print(b)
print(c)

#intercambiar valores
x,y = 10,20
print(x,y)
x,y=y,x
print(x,y)

nombre_completo = "Rafael Correa Mashi" #snake_case
nombreCompleto = "Rafael Correa Delgado" #NO USAR camelcase

MAX_REINTENTOS=3                         #Mayusculas SOSTENIDAS 
_variable_interna= "privada"             #Para uso interno


#Manejo de Enteros

pequeno= 42
negativo = -17
grande = 1_000_000_000
enorme= 2**100

print(pequeno)
print(negativo)
print(grande)
print(enorme)