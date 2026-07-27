// Concepto puro
type Ubicacion = [number, number];           
type HorarioVuelo = [string, string];        
type InformacionVuelo = [string, number];     

const coordenadasAeropuerto: Ubicacion = [-0.1292, -78.3575];
const horarioOperacion: HorarioVuelo = ["08:00", "10:30"];
const datosVuelo: InformacionVuelo = ["UIO101", 180];


const [latitud, longitud] = coordenadasAeropuerto;
const [horaSalida, horaLlegada] = horarioOperacion;
const [codigoVueloInfo, pasajerosVueloInfo] = datosVuelo;

console.log(`Ubicación: lat=${latitud}, lon=${longitud}`);
console.log(`Horario: ${horaSalida} - ${horaLlegada}`);
console.log(`Vuelo: ${codigoVueloInfo}, Pasajeros: ${pasajerosVueloInfo}`);

type HorarioTerminal = [apertura: number, cierre: number];
const horarioTerminalPrincipal: HorarioTerminal = [6, 22];