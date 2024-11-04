class producto {
    static contadorProductos = 0;
    constructor(nombre, precio) {
        this._idProducto = ++producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto() {
        return this._idProducto;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get precio() {
        return this._precio;
    }

    set precio(precio) {
        this._precio = precio;
    }

    toString() {
        return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`;
    }
}

class Orden {
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS() {
        return 5;
    }

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._Productos = [];
    }

    agregarProducto(producto) {
        if (this._Productos.length < Orden.getMAX_PRODUCTOS()) {
            this._Productos.push(producto);
        } else {
            console.log("No se pueden agregar más productos");
        }
    }

    calcularTotal() {
        let totalVenta = 0;
        for (let producto of this._Productos) {
            totalVenta += producto.precio;
        }
        return totalVenta;
    }

    mostrarOrden() {
        let productoOrden = "";
        for (let producto of this._Productos) {
            productoOrden += `{${producto.toString()}} `;
        }
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productoOrden}`);
    }
}

let producto1 = new producto('Pantalon', 200);
let producto2 = new producto('Camisa', 150);
let orden1 = new Orden();
console.log(producto1.toString());
console.log(producto2.toString());
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.mostrarOrden();
