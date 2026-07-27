aeropuerto = {
    "nombre": "Aeropuerto Quito",
    "ciudad": "Quito",
    "pistas": 2
}

vuelo = dict(codigo="AV123", origen="Quito", destino="Guayaquil")

print(aeropuerto["nombre"])
print(aeropuerto.get("telefono"))
print(aeropuerto.get("telefono", "No registrado"))

aeropuerto["telefono"] = "022345678"
aeropuerto["pistas"] = 3
del aeropuerto["ciudad"]

valor = aeropuerto.pop("telefono")
print(aeropuerto)

print("nombre" in aeropuerto)
print("ciudad" in aeropuerto)

print(aeropuerto.keys())
print(aeropuerto.values())
print(aeropuerto.items())

for clave, valor in aeropuerto.items():
    print(f"{clave}: {valor}")

aeropuerto.update({"ciudad": "Quito", "terminales": 4})
print(aeropuerto)

extra = {"internacional": True, "estado": "Operativo"}
completo = aeropuerto | extra
print(completo)

sistema = {
    "aeropuerto": "Quito",
    "vuelos": {
        1: {"codigo": "AV123", "destino": "Guayaquil"},
        2: {"codigo": "LA456", "destino": "Cuenca"}
    },
    "terminales": ["A", "B"]
}

print(sistema["vuelos"][1]["codigo"])

sistema["vuelos"][3] = {
    "codigo": "EQ789",
    "destino": "Manta"
}

aeropuerto.setdefault("pais", "Ecuador")
aeropuerto.setdefault("nombre", "Otro Aeropuerto")

print(aeropuerto)