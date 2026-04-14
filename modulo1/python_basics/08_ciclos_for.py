print("Ciclo for")
frutas=["manzana","banana","pera"]
for fruta in frutas:
    print(fruta)
print("Recorrrer Palabras")
for letra in "frutas":
    print(letra)
    
print("Recorrer rangos")
for i in range(1,5):
    print(i)
    
print("Recorrer rango configurando pasos")
for i in range(1,10,2):
    print(i)
    
print("Enumerar lista")
for i, fruta in enumerate(frutas):
    print(i, fruta)
    
    
print("Dos listas a la vez")
nombres=["Ana","Luis"]
edades=[20,25]
for nombre, edad in zip(nombres, edades):
    print(nombre,edad)

print("Control del Ciclo")
for i in range(10):
    if i==6:
        continue
    
    
print("Contro de ciclo Break")
for i in range(5):
    if i==3:
        break
    print(i)
print("continue")
for i in range(5):
    if i==2:
        continue
    print(i)
    
print("for anidado")
for i in range(3):
    for j in range(2):
        print(i,j)
print("Lista de comprehension forma corta ")
cuadrados = [x**2 for x in range (5)]
print(cuadrados)

ventas=[120,80,200,50,300]
for ventaspo in ventas:
    if (int(ventaspo)>100):
        if (int(ventaspo)>250):
            print("Tiene un bono de $30")
        else:
            print("Tiene un bono de $10")
    else:
        print("No se registra evntas mayores a 100")

    