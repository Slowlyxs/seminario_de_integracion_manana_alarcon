
const pasajeros: number      = 180;
const pista: number          = 12;
const temperatura: number    = 18.5;
const codigoAeropuerto: number = 0x01; 

const aeropuertos: string = "Aeropuerto Mariscal Sucre";
const ciudad: string     = 'Quito';
const destino: string    = `/vuelos/guayaquil`;


const pistaDisponible: boolean = true;
const vueloRetrasado: boolean  = false;
const embarqueAbierto: boolean = false;


const capacidad = 180;
const ocupados = 150;
const disponibles = capacidad - ocupados; // 30


const vuelo = "  UIO123  ";
console.log(vuelo.trim().toUpperCase());     // "UIO123"
console.log(aeropuerto.includes("Mariscal")); // true
console.log(destino.split("/")[2]);           // "guayaquil"

const puedeDespegar: boolean = pistaDisponible && !vueloRetrasado;
console.log(puedeDespegar); // true