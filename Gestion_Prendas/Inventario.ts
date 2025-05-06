import { Prenda } from './Prenda';
// import { Prenda } from './prenda'; // Asegúrate de que la ruta sea correcta
export class Inventario {
    private prendas: Prenda[] = [];

    agregarPrenda(prenda: Prenda): void {
        this.prendas.push(prenda);
        console.log('Prenda ${prenda.nombre} agregada al inventario.');
    }

    eliminarPrenda(nombre: string): void {
        this.prendas = this.prendas.filter(prenda => prenda.nombre !== nombre);
        console.log('Prenda ${nombre} eliminada del inventario.');
    }

    listarPrendas(): Prenda[] {
        return this.prendas;
    }

    buscarPrenda(nombre: string): Prenda | undefined {
        return this.prendas.find(prenda => prenda.nombre === nombre);
    }
}

