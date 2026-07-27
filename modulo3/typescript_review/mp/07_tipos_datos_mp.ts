// NUMÉRICO
// Concepto puro

const idPistaPrincipal: number = 12;
const climaActualTerminal: number = 22.5;
const alturaPistaNivelMar: number = -5;
const identificadorHex: number = 0xff;
const codigoBinPuerta: number = 0b1010;
const codigoOctTerminal: number = 0o17;
const totalViajerosAnuales: number = 1_000_000;

console.log(identificadorHex);
console.log(codigoBinPuerta);
console.log(totalViajerosAnuales);


console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.isFinite(1 / 0));
console.log(Number.isNaN(0 / 0));
const terminalPrincipal: string = "Terminal Internacional";
const ciudadDestinoFinal: string = "Guayaquil";
const descripcionRuta: string = `Ruta hacia ${"Cuenca"}`;

const codigoOperacion: string = "VUE-501";
const totalPasajerosVuelo: number = 180;

const resumenOperacion: string =
  `Código: ${codigoOperacion}. Pasajeros: ${totalPasajerosVuelo}.`;

const mensajeEmbarqueFinal: string =
  `Embarque ${totalPasajerosVuelo > 0 ? "habilitado" : "cerrado"}.`;

const reporteTerminalGeneral: string = `
Terminal : Internacional
Ciudad   : Quito
Estado   : Operativa
`.trim();

console.log("  VUE-501  ".trim());
console.log("quito".toUpperCase());
console.log("UIO-GYE-001".split("-"));
console.log("Aeropuerto Internacional".includes("Internacional"));
console.log("archivo.ts".endsWith(".ts"));
console.log("archivo.ts".startsWith(".ts"));

const puertaDisponibleSistema: boolean = true;
const mantenimientoPendiente: boolean = false;

const existenPasajeros = 180 > 0;
const existenPuertasLibres = 0 > 0;

if (!existenPuertasLibres) {
  console.log("No existen puertas disponibles");
}


let vueloPendienteAsignacion: undefined = undefined;
let pilotoDisponibleSistema: null = null;

function obtenerCodigoVuelo(idVuelo: number): string | null {
  if (idVuelo === 1) return "UIO501";
  return null;
}

const resultadoBusquedaVuelo = obtenerCodigoVuelo(5);

const codigoMostrado = resultadoBusquedaVuelo ?? "Sin vuelo registrado";
console.log(codigoMostrado);

const longitudCodigoVuelo = resultadoBusquedaVuelo?.length;
console.log(longitudCodigoVuelo);