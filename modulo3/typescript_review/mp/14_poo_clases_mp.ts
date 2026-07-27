// Concepto puro
class Ej11Vuelo {
  codigo: string;
  pasajeros: number;
  activo: boolean;

  constructor(codigo: string, pasajeros: number, activo: boolean) {
    this.codigo = codigo;
    this.pasajeros = pasajeros;
    this.activo = activo;
  }


  describir(): string {
    const estado = this.activo ? "operativo" : "cancelado";
    return `${this.codigo} — ${this.pasajeros} pasajeros (${estado})`;
  }
}

const ej11VueloQuito = new Ej11Vuelo("UIO101", 180, true);
const ej11VueloMadrid = new Ej11Vuelo("MAD202", 250, false);

console.log(ej11VueloQuito.describir());   
console.log(ej11VueloMadrid.describir()); 