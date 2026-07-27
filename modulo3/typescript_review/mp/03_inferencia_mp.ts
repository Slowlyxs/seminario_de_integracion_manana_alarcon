// ── Anotación explícita ───────────────────────────────────────────────────
// Tú le dices a TS cuál es el tipo.
const numeroPista: number = 12;
const nombreAeropuerto: string = "Mariscal Sucre";
const aeropuertoAbierto: boolean = true;


const numeroPista2 = 12;                 
const nombreAeropuerto2 = "Mariscal Sucre"; 
const aeropuertoAbierto2 = true;       

let capacidadTerminal: number;
capacidadTerminal = 500;


let codigoVuelo: number | string = 101;
codigoVuelo = "UIO101"; 


function registrarVuelo(destino: string, pasajeros: number): string {
  return `Vuelo hacia ${destino} con ${pasajeros} pasajero(s)`;
}

const tarifa = 90.88;