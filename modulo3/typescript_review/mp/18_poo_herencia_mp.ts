// Concepto puro
class Ej15VehiculoAereo {
  constructor(public codigo: string) {}

  describir(): string {
    return `${this.codigo} está listo para operar.`;
  }
}

class Ej15Avion extends Ej15VehiculoAereo {
  constructor(codigo: string, public modelo: string) {
    super(codigo);
  }


  override describir(): string {
    return `${this.codigo} está listo para despegar.`;
  }

  despegar(pista: string): string {
    return `${this.codigo} despega desde la pista ${pista}.`;
  }
}

const ej15Vehiculo = new Ej15VehiculoAereo("GEN-001");
const ej15AvionPrincipal = new Ej15Avion("UIO101", "Boeing 737");

console.log(ej15Vehiculo.describir());            
console.log(ej15AvionPrincipal.describir());      
console.log(ej15AvionPrincipal.despegar("P-01")); 
console.log(ej15AvionPrincipal.modelo);           