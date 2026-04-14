contador =1
while (contador <=5):
    print(f"contador: {contador}")
    contador+=1
    
print("Control de Ciclo")
print("continue")

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(f"contador: {i}")

print("Break")

i = 0
while i <= 5:
    i += 1
    if i == 3:
        break
    print(f"contador: {i}")

numero = int(input("Ingrese el numero: "))
while numero != 0:
    print("Ingresaste:", numero)
    numero = int(input("Ingrese numero: "))