class Producto {

    static contadorProductos = 0

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;     
        this._nombre = nombre;              
        this._precio = precio;              
    }

    // Métodos para obtener el idProducto
    get idProducto() {
        return this._idProducto;
    }

    // Métodos para obtener el nombre
    get nombre() {
        return this._nombre;
    }

    // Método para establecer el nombre
    set nombre(nombre) {
        this._nombre = nombre;
    }

    // Métodos para obtener el precio
    get precio() {
        return this._precio;
    }

    // Método para establecer el precio
    set precio(precio) {
        this._precio = precio;
    }

    // Método para representar el objeto como cadena
    toString() {
        return `Producto [ID: ${this.idProducto}, Nombre: ${this.nombre}, Precio: ${this.precio}]`;
    }
}


class Orden {

    static contadorOrdenes = 0
    static getMAX_PRODUCTOS(){
        return 5
    } 
    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;                      
        this._productos = [];  
        this._contadorProductosAgregados = 0;                                        
    }

    get idOrden() {
        return this._idOrden;
    }

    // Método para agregar un producto a la orden
    agregarProducto(producto) {
        if (this._productos.length < Orden.getMAX_PRODUCTOS()) {
            this._productos.push(producto); // Primera SINTAXIS
        //  this._productos[this._contadorProductosAgregados++] = producto  SEGUNDA SINTAXIS    
            console.log(`Producto agregado: ${producto._nombre}`);
        } else {
            console.log("No se puede agregar más productos a la orden. Límite alcanzado.");
        }
    }
    // Método para calcular el total de la orden
    calcularTotal() {
         let totalVenta = 0
        for(let producto of this._productos) {
            totalVenta += producto.precio;
        }
        return totalVenta;
    }

    // Método para mostrar la orden
    mostrarOrden() {
        let productosOrden = " ";
        for (let producto of this._productos) {
            productosOrden += "\n{" +producto.toString()+"}";
            
        }
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()},\nProductos: ${productosOrden}`)
    }
}

let p1 = new Producto("Camisa",1)
let p2 = new Producto("pantalon",1)

let orden1 = new Orden();

orden1.agregarProducto(p1);
orden1.agregarProducto(p2);
orden1.agregarProducto(p2);
orden1.agregarProducto(p2);
orden1.agregarProducto(p2);
orden1.agregarProducto(p2);


orden1.mostrarOrden();