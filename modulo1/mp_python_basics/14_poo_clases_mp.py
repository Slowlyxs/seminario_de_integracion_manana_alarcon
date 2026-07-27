class Vuelo:
    tipo = "Comercial"

    def __init__(self, codigo, destino):
        self.codigo = codigo
        self.destino = destino

    def mostrar_info(self):
        return f"Vuelo {self.codigo} con destino a {self.destino}."

    def cambiar_destino(self, nuevo_destino):
        self.destino = nuevo_destino
        print(f"El vuelo {self.codigo} ahora va hacia {self.destino}.")

    def __str__(self):
        return f"Vuelo({self.codigo}, {self.destino})"

    def __repr__(self):
        return f"Vuelo(codigo={self.codigo!r}, destino={self.destino!r})"

vuelo1 = Vuelo("AV123", "Guayaquil")
vuelo2 = Vuelo("LA456", "Cuenca")

print(vuelo1.mostrar_info())
print(vuelo2.mostrar_info())

vuelo1.cambiar_destino("Manta")

print(str(vuelo1))
print(repr(vuelo1))

print(Vuelo.tipo)