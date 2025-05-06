"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Inventario_1 = require("./Inventario");
const inventario = new Inventario_1.Inventario();
// Agregar prendas al inventario de ejemplo
inventario.agregarPrenda({
    nombre: "Camiseta",
    talla: "M",
    tipo: "camiseta",
    estado: "disponible",
    cantidad: 10 // Cantidad de camisetas disponibles
});
inventario.agregarPrenda({
    nombre: "Pantalón",
    talla: "L",
    tipo: "pantalon",
    estado: "disponible",
    cantidad: 5 // Cantidad de pantalones disponibles
});
// Listar prendas en el inventario
const prendas = inventario.listarPrendas();
console.log("Prendas en el inventario:");
prendas.forEach(prenda => {
    console.log(`- ${prenda.nombre} (${prenda.talla}, ${prenda.tipo}, ${prenda.estado})`);
});
// Buscar una prenda por nombre
const prendaBuscada = inventario.buscarPrenda("Camiseta");
if (prendaBuscada) {
    console.log(`Prenda encontrada: ${prendaBuscada.nombre} (${prendaBuscada.talla}, ${prendaBuscada.tipo}, ${prendaBuscada.estado})`);
}
else {
    console.log("Prenda no encontrada.");
}
// Eliminar una prenda del inventario   
inventario.eliminarPrenda("Camiseta");
console.log("Prenda eliminada del inventario.");
// Listar prendas después de la eliminación 
const prendasActualizadas = inventario.listarPrendas();
console.log("Prendas en el inventario después de la eliminación:");
prendasActualizadas.forEach(prenda => {
    console.log(`- ${prenda.nombre} (${prenda.talla}, ${prenda.tipo}, ${prenda.estado})`);
});
