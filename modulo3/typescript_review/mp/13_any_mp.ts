


let ej10DatoSistema: any = "UIO101";
ej10DatoSistema = 180;       // ok
ej10DatoSistema = true;      // ok
ej10DatoSistema.metodoInexistente();

let ej10RespuestaApi: unknown = "Aeropuerto Quito";
ej10RespuestaApi = 250; // ok, acepta cualquier valor



if (typeof ej10RespuestaApi === "string") {
  console.log(ej10RespuestaApi.toUpperCase()); // ok
}


function ej10LanzarErrorOperacion(mensaje: string): never {
  throw new Error(mensaje);
}

function ej10VerificarEstado(valor: never): never {
  throw new Error(`Caso no manejado: ${String(valor)}`);
}