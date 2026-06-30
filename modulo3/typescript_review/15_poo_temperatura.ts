class Temperatura {
  valorCelcius: number;
  valorFarenhei: number;

  constructor(celcius: number = 0, farenhei: number = 32) {
    this.valorCelcius = celcius;
    this.valorFarenhei = farenhei;
  }

  aFahrenheit(): number {
    return this.valorCelcius * 9 / 5 + 32;
  }

  aKelvin(): number {
    return this.valorCelcius + 273.15;
  }

  describir(): string {
    return `${this.valorCelcius}°C = ${this.aFahrenheit()}°F = ${this.aKelvin()}K`;
  }
}

const hervor = new Temperatura(100, 212);
const congelacion = new Temperatura(0, 32);