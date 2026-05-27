print("Funciones en Python")

print("Funcion basica")
def mostrar_vuelo():
    print("Vuelo registrado en el aeropuerto")
mostrar_vuelo()

print("Funcion con parametros")
def mostrar_destino(destino):
    print(f"Vuelo con destino a {destino}")
mostrar_destino("Quito")
mostrar_destino("Guayaquil")

print("Funcion con return")
def sumar_pasajeros(a,b):
    return a+b
print(sumar_pasajeros(120,80))

print("Parametros por posicion")
def registrar_vuelo(codigo,destino,puerta):
    print(f"{codigo},{destino},{puerta}")

registrar_vuelo("AV101","Quito","5")
registrar_vuelo(destino="Cuenca",codigo="AV202",puerta=3)

print("Parametros por defecto")
def estado_vuelo(vuelo, estado="Activo", terminal="Norte"):
    print(f"{vuelo} {estado} {terminal}")

estado_vuelo("AV101","Retrasado","Sur")
estado_vuelo("AV202",terminal="Internacional")
estado_vuelo("AV303","Finalizado")

print("Parametros posicionales")
def total_equipaje(*pesos):
    print(f"Pesos recibidos {pesos}")
    return sum(pesos)

print(total_equipaje(20,15,30))
print(total_equipaje(10,12,18,25))

print("Parametros combinados")
def mostrar_terminal(nombre,*vuelos):
    print(nombre)
    for vuelo in vuelos:
        print(f"- {vuelo}")

mostrar_terminal("Terminal Norte","AV101","AV202","AV303")

print("Parametros clave valor")
def crear_vuelo(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_vuelo(codigo="AV101",destino="Quito",pasajeros=120)

print("Combinacion de parametros")
def configurar_aeropuerto(nombre,*puertas,activo=True,**opciones):
    print(f"Aeropuerto: {nombre}")
    print(f"Puertas: {puertas}")
    print(f"Activo: {activo}")
    print(f"Opciones: {opciones}")

configurar_aeropuerto("Mariscal",1,2,3,seguridad=True,camaras=20)

print("Multiples valores")
def minimo_maximo(vuelos):
    return min(vuelos),max(vuelos)

minimo,maximo=minimo_maximo([10,20,30,40])
print(f"Minimo {minimo}, Maximo {maximo}")

_,maximo=minimo_maximo([100,120,90])
print(f"Solo maximo {maximo}")

print("Diccionario")
def analizar_vuelos(datos):
    total=sum(datos)
    n=len(datos)

    return{
        "total":total,
        "media":total/n if n>0 else 0,
        "minimo":min(datos) if datos else None,
        "maximo":max(datos) if datos else None
    }

vuelos=[120,80,200,150]
stats=analizar_vuelos(vuelos)

print(f"Total: {stats['total']}")
print(f"Media: {stats['media']}")
print(f"Rango: {stats['minimo']}-{stats['maximo']}")

print("Funciones lambda")
def doble_vuelo(x):
    return x*2

doble=lambda x:x*2

print(doble_vuelo(2))
print(doble(2))

suma=lambda a,b:a+b

print(suma(100,200))