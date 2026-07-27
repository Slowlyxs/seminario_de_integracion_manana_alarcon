
const nombreTerminal: string = "Terminal A";
const ciudadAeropuerto: string = "Quito";
const cantidadVuelos: number = 42;

const mensajeTerminal: string = `Terminal: ${nombreTerminal}. Ciudad: ${ciudadAeropuerto}. Vuelos programados: ${cantidadVuelos}.`;
console.log(mensajeTerminal);

const capacidadAvion: number = 180;
const pasajerosAbordo: number = 150;
const mensajeAsientos: string = `Asientos libres: ${capacidadAvion - pasajerosAbordo}`;
console.log(mensajeAsientos);

let codigoActualVuelo: string = "GYE205";
let estadoActualVuelo: boolean = true;
let porcentajeOcupacion: number = 88.7;

const reporteVueloBase: string = `
=== Reporte del vuelo ===
Código    : UIO101
Estado    : Activo
Ocupación : 90%
`;

const reporteVueloActual: string = `
=== Reporte del vuelo ===
Código    : ${codigoActualVuelo}
Estado    : ${estadoActualVuelo ? "Activo" : "Inactivo"}
Ocupación : ${porcentajeOcupacion}%
`;

console.log(reporteVueloActual);