print("match-case")
vuelo = input("Esto del vuelo es aterrizando, vuelo, despegando")
match vuelo:
    case "aterrizando":
        print("El vuelo está aterrizando")
    case "vuelo":
        print("El vuelo está en curso")
    case "despegando":
        print("El vuelo está despegando")
    case "reiniciar":
        print("reiniciando el sistema")
    case _:
        print(f"comando '{vuelo}'no encontrado")
        

print("Estado de vuelos")

pasajeros = 120
match pasajeros:
    case n if n < 50:
        print(f"{n} pasajeros - vuelo con poca ocupacion")
    case 50:
        print("Vuelo con ocupacion minima")
    case n if n % 2 == 0:
        print(f"{n} pasajeros - vuelo con ocupacion alta")
    case n:
        print(f"{n} pasajeros registrados")