class MensajeAeropuerto:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Las subclases deben implementar enviar()")

    def __str__(self):
        return f"{self.__class__.__name__} -> {self.destinatario}"

class MensajePantalla(MensajeAeropuerto):
    def enviar(self):
        return f"Pantalla: {self.mensaje}"

class MensajeAltavoz(MensajeAeropuerto):
    def enviar(self):
        return f"Altavoz: {self.mensaje}"

class MensajeSMS(MensajeAeropuerto):
    def enviar(self):
        return f"SMS a {self.destinatario}: {self.mensaje}"

class MensajeEmail(MensajeAeropuerto):
    def enviar(self):
        return f"Email a {self.destinatario}: {self.mensaje}"

def enviar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje.enviar())

avisos = [
    MensajePantalla("Terminal A", "Vuelo AV123 embarcando"),
    MensajeAltavoz("Pasajeros", "Diríjanse a la puerta 5"),
    MensajeSMS("0999999999", "Su vuelo ha sido reprogramado"),
    MensajeEmail("cliente@email.com", "Confirmación de vuelo")
]

print("Enviando mensajes:")
enviar_mensajes(avisos)

class SistemaEquipaje:
    def leer(self):
        return "equipaje registrado"

    def guardar(self, datos):
        print(f"Guardando equipaje: {datos}")

class SistemaVuelos:
    def leer(self):
        return "vuelos programados"

    def guardar(self, datos):
        print(f"Guardando vuelos: {datos}")

class SistemaPasajeros:
    def leer(self):
        return "pasajeros registrados"

    def guardar(self, datos):
        print(f"Guardando pasajeros: {datos}")

def procesar_sistema(sistema):
    datos = sistema.leer()
    print(f"Procesando {datos}")
    sistema.guardar(f"actualizacion_{datos}")

for sistema in [SistemaEquipaje(), SistemaVuelos(), SistemaPasajeros()]:
    procesar_sistema(sistema)