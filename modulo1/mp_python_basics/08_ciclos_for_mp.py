print("Ciclo for"); vuelos=["Quito","Guayaquil","Cuenca"]; 
for vuelo in vuelos: print(vuelo)

print("Recorrer palabra"); 
for letra in "aeropuerto": print(letra)

print("Recorrer rangos"); 
for i in range(1,5): print(i)

print("Rango con pasos"); 
for i in range(1,10,2): print(i)

print("Enumerar vuelos"); 
for i, vuelo in enumerate(vuelos): print(i, vuelo)

print("Dos listas"); pilotos=["Carlos","Luis"]; puertas=[1,2]
for piloto, puerta in zip(pilotos, puertas): print(piloto, puerta)

print("Control continue"); 
for i in range(10):
    if i==6: continue
    print(i)

print("Control break"); 
for i in range(5):
    if i==3: break
    print(i)

print("Continue"); 
for i in range(5):
    if i==2: continue
    print(i)

print("For anidado"); 
for i in range(3):
    for j in range(2):
        print(i,j)

print("Lista corta"); vuelosdobles=[x*2 for x in range(5)]; print(vuelosdobles)

pasajeros=[120,80,200,50,300]
for cantidad in pasajeros:
    if int(cantidad)>100:
        if int(cantidad)>250:
            print("Vuelo prioritario")
        else:
            print("Vuelo autorizado")
    else:
        print("Vuelo con baja ocupacion")