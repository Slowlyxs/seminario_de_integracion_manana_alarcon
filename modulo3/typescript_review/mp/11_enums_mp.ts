
enum Ej8EstadoOperacion {
  Programado, // 0
  Embarcando, // 1
  EnVuelo,    // 2
  Finalizado, // 3
}

const ej8EstadoActual: Ej8EstadoOperacion = Ej8EstadoOperacion.Programado;
console.log(ej8EstadoActual);         
console.log(Ej8EstadoOperacion[0]);      

enum Ej8CodigoTerminal {
  Nacional = 100,
  Internacional = 200,
  Carga = 300,
}

enum Ej8TipoAcceso {
  Pasajeros = "PASAJEROS",
  Tripulacion = "TRIPULACION",
  Mantenimiento = "MANTENIMIENTO",
}

const ej8AccesoActual: Ej8TipoAcceso = Ej8TipoAcceso.Tripulacion;
console.log(ej8AccesoActual); // "TRIPULACION"