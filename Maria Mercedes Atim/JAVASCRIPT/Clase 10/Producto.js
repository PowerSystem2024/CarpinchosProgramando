class Producto {
    static contadorProductos = 0;

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    // Método para obtener el ID del producto
    getIdProducto() {
        return this._idProducto;
    }

    // Método para obtener el nombre del producto
    getNombre() {
        return this._nombre;
    }

    // Método para establecer el nombre del producto
    setNombre(nombre) {
        this._nombre = nombre;
    }

    // Método para obtener el precio del producto
    getPrecio() {
        return this._precio;
    }

    // Método para establecer el precio del producto
    setPrecio(precio) {
        if (precio >= 0) {
            this._precio = precio;
        } else {
            console.error("El precio no puede ser negativo.");
        }
    }

    // Método toString
    toString() {
        return `Producto ID: ${this._idProducto}, Nombre: ${this._nombre}, Precio: ${this._precio}`;
    }
}

let producto1 = new Producto("Pantalon", 200);
let producto2 = new Producto("Camisa", 150);
console.log(producto1.toString());
console.log(producto2.toString());