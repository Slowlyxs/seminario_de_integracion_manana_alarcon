interface Ej17Serializable {
  serializar(): string;
}

interface Ej17Validable {
  esValido(): boolean;
}

class Ej17Vuelo implements Ej17Serializable, Ej17Validable {
  constructor(
    public codigo: string,
    public pasajeros: string[],
    public capacidad: number
  ) {}

  serializar(): string {
    return JSON.stringify({
      codigo: this.codigo,
      pasajeros: this.pasajeros,
      capacidad: this.capacidad,
    });
  }

  esValido(): boolean {
    return this.pasajeros.length > 0 && this.capacidad > 0;
  }
}

const ej17VueloPrincipal = new Ej17Vuelo(
  "UIO101",
  ["Juan", "María"],
  180
);

console.log(ej17VueloPrincipal.esValido());
console.log(ej17VueloPrincipal.serializar());
