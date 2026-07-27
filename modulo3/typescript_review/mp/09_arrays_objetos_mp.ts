// Concepto puro
type VueloProgramado = {
  id: number;
  destino: string;
  pasajeros: number;
  activo: boolean;
  internacional: boolean;
};

const listaProgramacion: VueloProgramado[] = [
  { id: 1, destino: "Quito",      pasajeros: 180, activo: true,  internacional: false },
  { id: 2, destino: "Guayaquil",  pasajeros: 150, activo: true,  internacional: false },
  { id: 3, destino: "Madrid",     pasajeros: 220, activo: false, internacional: true },
  { id: 4, destino: "Cuenca",     pasajeros: 90,  activo: true,  internacional: false },
  { id: 5, destino: "Bogotá",     pasajeros: 170, activo: true,  internacional: true },
];

const vuelosActivos: VueloProgramado[] = listaProgramacion.filter((v) => v.activo);
const destinosVuelos: string[] = listaProgramacion.map((v) => v.destino);
const vueloMenorPasajeros: VueloProgramado | undefined = listaProgramacion.reduce((min, v) =>
  v.pasajeros < min.pasajeros ? v : min
);

console.log(destinosVuelos);
console.log(vueloMenorPasajeros?.destino);
console.log(vuelosActivos.length);
console.log("Lista completa de vuelos:", listaProgramacion);

const cuartoVuelo = listaProgramacion[3];
if (cuartoVuelo) {
  console.log("El 4to vuelo existe:", cuartoVuelo.destino);
} else {
  console.log("El 4to vuelo no existe");
}