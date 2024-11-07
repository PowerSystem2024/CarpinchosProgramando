package ar.com.codesystem.ventas;

public class Orden {

    private int idOrden;
    private Producto productos[];
    private static int contadorOrdenes; // Contador estático de órdenes creadas
    private int contadorProductos; // Contador de productos en la orden
    private static final int MAX_PRODUCTOS = 10;

    public Orden() { // Constructor de la clase Orden
        this.idOrden = ++Orden.contadorOrdenes; // Asigna un ID único a la orden
        this.productos = new Producto[Orden.MAX_PRODUCTOS]; // Inicializa el arreglo de productos
    }

    public void agregarProducto(Producto producto){ // Método para agregar un producto a la orden
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){ // Verifica si hay espacio para más productos
            this.productos[this.contadorProductos++] = producto; // Agrega el producto al arreglo y aumenta el contador
        }
        else{ // Si se supera el máximo de productos
            System.out.println("Se ha superado el maximo de productos: " + Orden.MAX_PRODUCTOS + " productos."); // Mensaje de error
        }
    }

    public double calcularTotal(){ // Método para calcular el total de la orden
        double total = 0; // Variable para acumular el total
        for (int i = 0; i < this.contadorProductos; i++) { // Recorre los productos en la orden
            total += this.productos[i].getPrecio(); // Suma el precio de cada producto al total
        }
        return total; // Retorna el total calculado
    }

    public void mostrarOrden() { // Método para mostrar los detalles de la orden
        StringBuilder sb = new StringBuilder(); // Crea un StringBuilder para construir la salida por consola
        sb.append("idOrden: ").append(idOrden).append("\n"); // Agregamos el ID de la orden
        double totalOrden = calcularTotal(); // guardamos en la variable totalOrden el resultado del calculo total.
        sb.append("El total de la orden es: $").append(totalOrden).append("\n"); // Agrega el total de la orden
        sb.append("Productos de la Orden: \n"); // Encabezado para los productos
        for (int i = 0; i < this.contadorProductos; i++) { // Recorre los productos en la orden
            sb.append(this.productos[i]).append("\n"); // Agrega cada producto al StringBuilder
        }
        System.out.println(sb.toString()); // Muestra el contenido del StringBuilder
    }

}