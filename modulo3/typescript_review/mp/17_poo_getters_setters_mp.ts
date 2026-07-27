// Concepto puro
class Ej14Pista {
  private _longitud: number;

  constructor(longitud: number) {
    this._longitud = longitud;
  }

  get longitud(): number {
    return this._longitud;
  }

  set longitud(valor: number) {
    if (valor <= 0) throw new Error("La longitud debe ser positiva");
    this._longitud = valor;
  }

  get longitudKilometros(): number {
    return this._longitud / 1000;
  }
}

const ej14PistaPrincipal = new Ej14Pista(3500);

console.log(ej14PistaPrincipal.longitud);           
console.log(ej14PistaPrincipal.longitudKilometros);    

ej14PistaPrincipal.longitud = 4200;

console.log(ej14PistaPrincipal.longitudKilometros);   
