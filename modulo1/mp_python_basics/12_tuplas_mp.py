
vuelo = ("AV123", "Quito", "Guayaquil")
piloto = ("Carlos Pérez", 45, "Ecuador")
pista = 1, "Disponible"

print(type(pista))

print(vuelo[0])
print(vuelo[-1])
print(vuelo[1:])

codigo, origen, destino = vuelo
print(codigo, origen, destino)

principal, *otros = ("AV123", "AV456", "AV789", "AV999")
print(principal)
print(otros)

*restantes, ultimo = ("Puerta A1", "Puerta A2", "Puerta A3")
print(restantes)
print(ultimo)

def verificar_capacidad(capacidad, pasajeros):
    if pasajeros > capacidad:
        return False, "Capacidad excedida"
    return True, None

estado, error = verificar_capacidad(180, 150)

if error:
    print(error)
else:
    print("Embarque permitido")

ubicaciones = {
    ("Terminal 1", "Puerta A1"): "Vuelo nacional",
    ("Terminal 2", "Puerta B3"): "Vuelo internacional"
}

print(ubicaciones[("Terminal 1", "Puerta A1")])