
class PersonalAeropuerto:
    def __init__(self, nombre, turno, edad):
        self.nombre = nombre
        self.turno = turno
        self.edad = edad
        self._horas_trabajadas = 0

    def registrar_horas(self, horas):
        self._horas_trabajadas += horas
        return self

    def __str__(self):
        return f"{self.nombre} - Turno {self.turno} - {self._horas_trabajadas} horas"

class Piloto(PersonalAeropuerto):
    def __init__(self, nombre, turno, edad, licencia):
        super().__init__(nombre, turno, edad)
        self.licencia = licencia

    def volar(self):
        return f"{self.nombre} está pilotando un avión"

    def __str__(self):
        return f"{super().__str__()} - Licencia {self.licencia}"

class ControladorAereo(PersonalAeropuerto):
    def __init__(self, nombre, turno, edad, torre):
        super().__init__(nombre, turno, edad)
        self.torre = torre

    def dirigir_trafico(self):
        return f"{self.nombre} dirige el tráfico aéreo"

    def __str__(self):
        return f"{super().__str__()} - Torre {self.torre}"

class PilotoSenior(Piloto):
    def __init__(self, nombre, turno, edad, licencia, experiencia):
        super().__init__(nombre, turno, edad, licencia)
        self.__experiencia = experiencia
        self.__nivel = "Senior"

    def ascender(self):
        self.__nivel = "Supervisor"
        return self

    @property
    def experiencia(self):
        return self.__experiencia

    def __str__(self):
        return f"{super().__str__()} | Nivel: {self.__nivel} | Experiencia: {self.__experiencia} años"

piloto = PilotoSenior("Carlos", "Mañana", 45, "P123", 20)
piloto.registrar_horas(8)

print(piloto)

print(isinstance(piloto, PilotoSenior))
print(isinstance(piloto, Piloto))
print(isinstance(piloto, PersonalAeropuerto))
print(isinstance(piloto, ControladorAereo))

print(PilotoSenior.__mro__)