"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Inventario = void 0;
// import { Prenda } from './prenda'; // Asegúrate de que la ruta sea correcta
class Inventario {
    constructor() {
        this.prendas = [];
    }
    agregarPrenda(prenda) {
        this.prendas.push(prenda);
        console.log('Prenda ${prenda.nombre} agregada al inventario.');
    }
    eliminarPrenda(nombre) {
        this.prendas = this.prendas.filter(prenda => prenda.nombre !== nombre);
        console.log('Prenda ${nombre} eliminada del inventario.');
    }
    listarPrendas() {
        return this.prendas;
    }
    buscarPrenda(nombre) {
        return this.prendas.find(prenda => prenda.nombre === nombre);
    }
}
exports.Inventario = Inventario;
