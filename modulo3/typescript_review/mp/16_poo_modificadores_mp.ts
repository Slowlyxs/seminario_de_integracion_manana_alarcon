// Concepto puro
class Ej13Avion {
  readonly matricula: string;    
  public modelo: string;       
  private capacidad: number;      
  protected estado: string;     
  constructor(matricula: string, modelo: string, capacidadInicial: number) {
    this.matricula = matricula;
    this.modelo = modelo;
    this.capacidad = capacidadInicial;
    this.estado = "Disponible";
  }

  obtenerCapacidad(): number {
    return this.capacidad;
  }

  agregarCapacidad(cantidad: number): void {
    if (cantidad <= 0) throw new Error("Cantidad inválida");
    this.capacidad += cantidad;
  }
}

const ej13AvionPrincipal = new Ej13Avion(
  "HC-ABC",
  "Boeing 737",
  180
);

console.log(ej13AvionPrincipal.modelo);              
console.log(ej13AvionPrincipal.matricula);          
console.log(ej13AvionPrincipal.obtenerCapacidad()); 

ej13AvionPrincipal.agregarCapacidad(20);

console.log(ej13AvionPrincipal.obtenerCapacidad());
