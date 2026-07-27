let ej10DatoSistema: any = "UIO101";
ej10DatoSistema = 180;
ej10DatoSistema = true;

console.log("Dato del sistema:", ej10DatoSistema);

let ej10RespuestaApi: unknown = "Aeropuerto Quito";

if (typeof ej10RespuestaApi === "string") {
  console.log(ej10RespuestaApi.toUpperCase());
}

ej10RespuestaApi = 250;

if (typeof ej10RespuestaApi === "number") {
  console.log("Respuesta numérica:", ej10RespuestaApi);
}

function ej10LanzarErrorOperacion(mensaje: string): never {
  throw new Error(mensaje);
}

function ej10VerificarEstado(valor: never): never {
  throw new Error(`Caso no manejado: ${String(valor)}`);
}