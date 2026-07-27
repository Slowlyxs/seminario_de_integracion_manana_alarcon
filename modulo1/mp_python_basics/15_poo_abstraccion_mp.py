
from abc import ABC, abstractmethod

class VehiculoAeropuerto(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def capacidad(self):
        pass

    @abstractmethod
    def funcion(self):
        pass

    def describir(self):
        return f"{self.nombre}: capacidad={self.capacidad()}, función={self.funcion()}"

class Autobus(VehiculoAeropuerto):
    def __init__(self, nombre, pasajeros):
        super().__init__(nombre)
        self.pasajeros = pasajeros

    def capacidad(self):
        return self.pasajeros

    def funcion(self):
        return "Transportar pasajeros"

class CamionEquipaje(VehiculoAeropuerto):
    def __init__(self, nombre, maletas):
        super().__init__(nombre)
        self.maletas = maletas

    def capacidad(self):
        return self.maletas

    def funcion(self):
        return "Transportar equipaje"

class VehiculoCombustible(VehiculoAeropuerto):
    def __init__(self, nombre, litros):
        super().__init__(nombre)
        self.litros = litros

    def capacidad(self):
        return self.litros

    def funcion(self):
        return "Abastecer combustible"

vehiculos = [
    Autobus("Bus A1", 50),
    CamionEquipaje("Camión B1", 200),
    VehiculoCombustible("Cisterna C1", 5000)
]

for vehiculo in vehiculos:
    print(vehiculo.describir())

capacidad_total = sum(v.capacidad() for v in vehiculos)
print(f"Capacidad total: {capacidad_total}")