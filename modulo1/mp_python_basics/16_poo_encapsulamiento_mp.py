# encapsulamiento.py

class Vuelo:
    def __init__(self, codigo, capacidad=0):
        self.codigo = codigo
        self.__pasajeros = 0
        self.__capacidad = capacidad
        self.__historial = []
        self.__activo = True
        self.__registrar(f"Vuelo creado con capacidad para {capacidad} pasajeros")

    @property
    def pasajeros(self):
        return self.__pasajeros

    @property
    def activo(self):
        return self.__activo

    @property
    def historial(self):
        return list(self.__historial)

    def embarcar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if self.__pasajeros + cantidad > self.__capacidad:
            raise ValueError("Capacidad excedida")
        self.__pasajeros += cantidad
        self.__registrar(f"Embarcaron {cantidad} pasajeros")
        return self

    def desembarcar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__pasajeros:
            raise ValueError("No hay suficientes pasajeros")
        self.__pasajeros -= cantidad
        self.__registrar(f"Desembarcaron {cantidad} pasajeros")
        return self

    def transferir_pasajeros(self, destino, cantidad):
        self.desembarcar(cantidad)
        destino.embarcar(cantidad)
        self.__registrar(f"Transferidos {cantidad} pasajeros al vuelo {destino.codigo}")
        return self

    def __registrar(self, evento):
        self.__historial.append(evento)

    def __str__(self):
        return f"Vuelo({self.codigo}: {self.__pasajeros}/{self.__capacidad} pasajeros)"

vuelo1 = Vuelo("AV123", 200)
vuelo2 = Vuelo("LA456", 150)

vuelo1.embarcar(100).embarcar(20)
vuelo1.transferir_pasajeros(vuelo2, 30)

print(vuelo1)
print(vuelo2)
print(f"Pasajeros en vuelo 1: {vuelo1.pasajeros}")

for entrada in vuelo1.historial:
    print(entrada)