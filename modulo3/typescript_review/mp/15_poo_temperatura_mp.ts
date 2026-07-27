class Ej12Vuelo {
  duracionHoras: number;
  duracionMinutos: number;

  constructor(horas: number = 0, minutos: number = 0) {
    this.duracionHoras = horas;
    this.duracionMinutos = minutos;
  }

  aMinutos(): number {
    return this.duracionHoras * 60 + this.duracionMinutos;
  }

  aSegundos(): number {
    return this.aMinutos() * 60;
  }

  describir(): string {
    return `${this.duracionHoras}h ${this.duracionMinutos}min = ${this.aMinutos()} minutos = ${this.aSegundos()} segundos`;
  }
}

const ej12VueloNacional = new Ej12Vuelo(1, 30);
const ej12VueloInternacional = new Ej12Vuelo(8, 45);

console.log(ej12VueloNacional.describir());


console.log(ej12VueloInternacional.describir());
