export type TipoPrenda = 'camiseta' | 'pantalon' | 'chaqueta' | 'abrigo' | 'falda' | 'vestido' |
 'abrigo de piel' | 'abrigo de lana' | 'abrigo de plumas' | 'abrigo de cuero';
export type Disponibilidad = 'disponible' | 'no disponible';

export interface Prenda {
    nombre: string;
    talla: string;
    tipo: TipoPrenda;
    estado: Disponibilidad;
    cantidad: number; // Cantidad de prendas del mismo tipo
}

