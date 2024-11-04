class Orden {
    static contadorOrdenes = 0; // Contador estático de órdenes
    static MAX_PRODUCTOS = 5;    // Máximo de productos por orden

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes; // Asigna un ID único a la orden
        this.productos = []; // Arreglo para almacenar los productos de la orden
        this.contadorProductosAgregados = 0; // Contador de productos agregados a la orden
    }

    // Método para agregar un producto a la orden
    agregarProducto(producto) {
        if (this.contadorProductosAgregados < Orden.MAX_PRODUCTOS) { // Verifica si no se ha alcanzado el máximo
            this.productos.push(producto); // Agrega el producto al arreglo
            this.contadorProductosAgregados++; // Incrementa el contador
        } else {
            console.error("No se pueden agregar más productos a la orden."); // Mensaje de error si se supera el máximo
        }
    }

    // Método para calcular el total de la orden
    calcularTotal() {
        return this.productos.reduce((total, producto) => total + producto.getPrecio(), 0); // Suma los precios de los productos
    }

    // Método para mostrar la orden
    mostrarOrden() {
        console.log(`Orden ID: ${this._idOrden}`); // Muestra el ID de la orden
        this.productos.forEach(producto => { // Itera sobre los productos
            console.log(producto.toString()); // Muestra la representación en cadena de cada producto
        });
        console.log(`Total: ${this.calcularTotal()}`); // Muestra el total de la orden
    }
}
