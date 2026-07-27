abstract class Ej16ZonaAeropuerto {
  abstract capacidad(): number;
  abstract longitud(): number;

  describir(): string {
    return (
      `Capacidad: ${this.capacidad().toFixed(2)} | ` +
      `Longitud: ${this.longitud().toFixed(2)} m`
    );
  }
}

class Ej16Pista extends Ej16ZonaAeropuerto {
  constructor(private metros: number) {
    super();
  }

  override capacidad(): number {
    return this.metros / 10;
  }

  override longitud(): number {
    return this.metros;
  }
}

class Ej16Terminal extends Ej16ZonaAeropuerto {
  constructor(private puertas: number, private promedioPasajeros: number) {
    super();
  }

  override capacidad(): number {
    return this.puertas * this.promedioPasajeros;
  }

  override longitud(): number {
    return this.puertas * 25;
  }
}

const ej16PistaPrincipal = new Ej16Pista(3200);
const ej16TerminalPrincipal = new Ej16Terminal(8, 150);

console.log(ej16PistaPrincipal.describir());
console.log(ej16TerminalPrincipal.describir());