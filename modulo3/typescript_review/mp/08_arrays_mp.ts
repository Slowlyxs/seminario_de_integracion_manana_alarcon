// Concepto puro — dos sintaxis equivalentes
const listaVuelos: string[] = ["UIO101", "GYE202", "CUE303", "MEC404"];
const listaTerminales: Array<string> = ["A", "B", "C"];

// TypeScript infiere el tipo del array si lo inicializas
const capacidadAviones = [120, 180, 150]; // number[] inferido

// Métodos tipados: el compilador conoce el tipo del elemento
const capacidadesDobles: number[] = capacidadAviones.map((c) => c * 2);
const capacidadesMayores: number[] = capacidadAviones.filter((c) => c > 140);
const totalCapacidad: number = capacidadAviones.reduce((acc, c) => acc + c, 0);

console.log(`Capacidades dobles: ${capacidadesDobles}`);
console.log(`Capacidades mayores: ${capacidadesMayores}`);
console.log(`Capacidad total: ${totalCapacidad}`);

listaVuelos.push("LOH505");
console.log(`Lista de vuelos: ${listaVuelos}`);

listaVuelos.unshift("UIO001");
console.log(`Lista de vuelos: ${listaVuelos}`);

let ultimoVuelo = listaVuelos.pop();
console.log(`Lista de vuelos: ${listaVuelos}`);

let primerVuelo = listaVuelos.shift();
console.log(`Lista de vuelos: ${listaVuelos}`);

// Búsqueda
let existeVuelo: boolean = listaVuelos.includes("GYE202");
console.log(`Existe GYE202: ${existeVuelo}`);

let indiceVuelo: number = listaVuelos.indexOf("GYE202");
console.log(`Posición de GYE202: ${indiceVuelo}`);

let vueloEncontrado: string | undefined = listaVuelos.find((v) =>
  v.startsWith("CUE")
);
console.log(`Vuelo encontrado: ${vueloEncontrado}`);