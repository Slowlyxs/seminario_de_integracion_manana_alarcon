class Ej18Vehiculo {
  nombre(): string {
    return "Vehículo";
  }

  capacidad(): number {
    return 0;
  }
}

class Ej18Avion extends Ej18Vehiculo {
  constructor(private pasajeros: number) {
    super();
  }

  override nombre(): string {
    return "Avión";
  }

  override capacidad(): number {
    return this.pasajeros;
  }
}

class Ej18Helicoptero extends Ej18Vehiculo {
  constructor(private pasajeros: number) {
    super();
  }

  override nombre(): string {
    return "Helicóptero";
  }

  override capacidad(): number {
    return this.pasajeros;
  }
}

class Ej18Dron extends Ej18Vehiculo {
  constructor(private carga: number) {
    super();
  }

  override nombre(): string {
    return "Dron";
  }

  override capacidad(): number {
    return this.carga;
  }
}

const ej18Vehiculos: Ej18Vehiculo[] = [
  new Ej18Avion(180),
  new Ej18Helicoptero(12),
  new Ej18Dron(50),
];

for (const vehiculo of ej18Vehiculos) {
  console.log(
    `${vehiculo.nombre()}: capacidad = ${vehiculo.capacidad()}`
  );
}
