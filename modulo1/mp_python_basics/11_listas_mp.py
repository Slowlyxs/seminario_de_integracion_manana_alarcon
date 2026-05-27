print("Listas")

print("Crear listas")
vacia=[]
print(vacia)

vuelos=[101,202,303,404]
print(vuelos)

destinos=["Quito","Guayaquil","Cuenca","Manta"]
print(destinos)

mixta=[101,"Quito",True,None,25.5]
print(mixta)

anidada=[1,[2,3,4],5,6]
print(anidada)

print("Acceso a elementos")
print(destinos[0])
print(destinos[-1])
print(destinos[1:3])
print(destinos[::-1])

print("CRUD de lista")
terminales=["Norte","Sur","Carga"]

terminales.append("Internacional")
print(terminales)

terminales.insert(1,"VIP")
print(terminales)

terminales.extend(["Privada","Emergencia"])
print(terminales)

terminales[0]="Principal"
print(terminales)

terminales.remove("VIP")
print(terminales)

eliminado=terminales.pop()
print(terminales)

eliminado2=terminales.pop(0)
print(terminales)

del terminales[0]
print(terminales)

print("Buscar elementos")
print("Carga" in terminales)
print(terminales.index("Internacional"))
print(terminales.count("Carga"))

print("Ordenar lista")
pasajeros=[120,80,200,50,300]
print(pasajeros)

pasajeros.sort()
print(pasajeros)

pasajeros.sort(reverse=True)
print(pasajeros)

ordenada=sorted(pasajeros)
print(pasajeros)
print(ordenada)