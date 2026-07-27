// const — valor que NO cambia (preferida por defecto)
const CODIGO_AEROPUERTO: string = "UIO";
const NOMBRE_AEROPUERTO: string = "Aeropuerto Internacional Mariscal Sucre";
const AEROPUERTO_ACTIVO: boolean = true;

let vuelosProgramados: number = 0;
let estadoPista: string = "cerrada";
let vueloAutorizado: boolean = false;

console.log(`vuelos: ${vuelosProgramados} estado pista: ${estadoPista} vuelo autorizado: ${vueloAutorizado}`);

vuelosProgramados++;             // 1
estadoPista = "abierta";         // ok
vueloAutorizado = true;          // ok

console.log(`vuelos: ${vuelosProgramados} estado pista: ${estadoPista} vuelo autorizado: ${vueloAutorizado}`);
