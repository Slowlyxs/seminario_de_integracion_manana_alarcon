contador=1
while(contador<=5):
    print(f"Vuelo: {contador}")
    contador+=1

print("Control de ciclo")
print("continue")

i=0
while i<=5:
    i+=1
    if i==3:
        continue
    print(f"Puerta: {i}")

print("Break")

i=0
while i<=5:
    i+=1
    if i==3:
        break
    print(f"Terminal: {i}")

pasajeros=int(input("Ingrese cantidad de pasajeros: "))
while pasajeros!=0:
    print("Pasajeros registrados:", pasajeros)
    pasajeros=int(input("Ingrese cantidad de pasajeros: "))