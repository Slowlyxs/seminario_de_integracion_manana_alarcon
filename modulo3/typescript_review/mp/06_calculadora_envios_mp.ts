

type TipoVuelo = "nacional" | "internacional" | "regional";

interface Vuelo {
  destino: string;
  pasajeros: number;
  precioBoleto: number;
  tipo: TipoVuelo;
}

const TARIFAS: Record<TipoVuelo, number> = {
  nacional: 20.00,       
  internacional: 50.00,
  regional: 10.00,
};

const IMPUESTO_PCT = 0.12; // 12%

function calcularTarifa(vuelo: Vuelo): string {
  const tarifaBase = TARIFAS[vuelo.tipo];
  const costoPasajeros = tarifaBase * vuelo.pasajeros;
  const impuesto = vuelo.precioBoleto * IMPUESTO_PCT;
  const total = costoPasajeros + impuesto;

  return `
🛫 Tarifa del vuelo
   Destino      : ${vuelo.destino}
   Pasajeros    : ${vuelo.pasajeros}
   Tipo         : ${vuelo.tipo}
   Tarifa       : $${costoPasajeros.toFixed(2)}
   Impuesto     : $${impuesto.toFixed(2)}
   ─────────────────────────
   TOTAL        : $${total.toFixed(2)}
  `.trim();
}

const vuelo1: Vuelo = {
  destino: "Guayaquil",
  pasajeros: 120,
  precioBoleto: 150,
  tipo: "nacional",
};

const vuelo2: Vuelo = {
  destino: "Madrid",
  pasajeros: 80,
  precioBoleto: 950,
  tipo: "internacional",
};

console.log(calcularTarifa(vuelo1));
console.log("---");
console.log(calcularTarifa(vuelo2));
