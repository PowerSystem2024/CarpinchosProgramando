class Producto {
    static contadorProductos = 0; // Contador estático para asignar IDs únicos a los productos

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos; // Asigna un ID único al producto
        this._nombre = nombre; // Inicializa el nombre del producto
        this._precio = precio; // Inicializa el precio del producto
    }

    // Método para obtener el ID del producto
    getIdProducto() {
        return this._idProducto; // Devuelve el ID del producto
    }

    // Método para obtener el nombre del producto
    getNombre() {
        return this._nombre; // Devuelve el nombre del producto
    }

    // Método para establecer el nombre del producto
    setNombre(nombre) {
        this._nombre = nombre; // Establece el nuevo nombre del producto
    }

    // Método para obtener el precio del producto
    getPrecio() {
        return this._precio; // Devuelve el precio del producto
    }

    // Método para establecer el precio del producto
    setPrecio(precio) {
        if (precio >= 0) {
            this._precio = precio; // Establece el nuevo precio del producto
        } else {
            console.error("El precio no puede ser negativo."); // Mensaje de error si el precio es negativo
        }
    }

    // Método toString que devuelve una representación en cadena del producto
    toString() {
        return `Producto ID: ${this._idProducto}, Nombre: ${this._nombre}, Precio: ${this._precio}`; // Retorna la descripción del producto
    }
}

class Orden {
    static contadorOrdenes = 0; // Contador estático de órdenes

    static get MAX_PRODUCTOS() {
        return 5; // Máximo de productos por orden
    }

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes; // Asigna un ID único a la orden
        this.productos = []; // Arreglo para almacenar los productos de la orden
        this.contadorProductosAgregados = 0; // Contador de productos agregados a la orden
    }

    // Método para agregar un producto a la orden
    agregarProducto(producto) {
        if (this.contadorProductosAgregados < Orden.MAX_PRODUCTOS) { // Verificamos si no se ha alcanzado el máximo
            this.productos.push(producto); // Agregamos el producto al arreglo
            this.contadorProductosAgregados++; // Incrementamos el contador
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
        console.log(`Total: $${this.calcularTotal()}`); // Muestra el total de la orden
    }
}

// Creamos productos
let producto1 = new Producto("Pantalon", 200);
let producto2 = new Producto("Camisa", 150);
let producto3 = new Producto("Cinturon", 50);

// Creamos una nueva orden
let orden1 = new Orden();
let orden2 = new Orden();

// Agregamos los productos instanciados a la orden
orden1.agregarProducto(producto1); // Agregamos el pantalón
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden2.agregarProducto(producto1);
orden2.agregarProducto(producto2);
orden2.agregarProducto(producto3);

// Mostramos la orden
orden1.mostrarOrden(); // Mostramos los detalles de la orden, incluidos los productos y el total
console.log();
orden2.mostrarOrden();