type Ej9EstadoVuelo =
  | "programado"
  | "abordando"
  | "en_vuelo"
  | "aterrizado";

type Ej9PrioridadOperacion = "baja" | "media" | "alta";

function ej9ActualizarVuelo(
  id: number,
  estado: Ej9EstadoVuelo
): void {
  console.log(`Vuelo #${id}: ${estado}`);
}

ej9ActualizarVuelo(1, "abordando"); // ok


type Ej9NivelAlerta =
  | "baja"
  | "media"
  | "alta"
  | "critica";

interface Ej9Alerta {
  id: number;
  descripcion: string;
  prioridad: Ej9NivelAlerta;
  atendida: boolean;
}

function ej9MostrarAlerta(a: Ej9Alerta): string {
  const iconos: Record<Ej9NivelAlerta, string> = {
    baja: "⚪",
    media: "🟡",
    alta: "🟠",
    critica: "🔴",
  };

  const estado = a.atendida ? "✅" : "⏳";
  return `${estado} ${iconos[a.prioridad]} [#${a.id}] ${a.descripcion}`;
}

const ej9Alertas: Ej9Alerta[] = [
  {
    id: 1,
    descripcion: "Puerta de embarque ocupada",
    prioridad: "baja",
    atendida: true,
  },
  {
    id: 2,
    descripcion: "Pista fuera de servicio",
    prioridad: "critica",
    atendida: false,
  },
  {
    id: 3,
    descripcion: "Retraso en el embarque",
    prioridad: "media",
    atendida: false,
  },
];

for (const alerta of ej9Alertas) {
  console.log(ej9MostrarAlerta(alerta));
}