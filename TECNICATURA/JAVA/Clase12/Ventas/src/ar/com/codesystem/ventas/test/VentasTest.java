
package ar.com.codesystem.ventas.test;
// Importación de clases
import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        // Creación de objetos
        // Clase Producto
        Producto producto1 = new Producto("Pantalón", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        // Clase Orden
        Orden orden1 = new Orden();
        
        // Se agregan productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        
        orden1.mostrarOrden();
        
        /*
        TAREA:
            1. Crear más objetos de tipo Producto = 10
            2. Crear más objetos de tipo Orden = 2
        */
        Producto producto3 = new Producto("Zapatillas", 45000.00);
        Producto producto4 = new Producto("Cinturón", 2500.00);
        Producto producto5 = new Producto("Medias", 500.00);

        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        
        Producto producto6 = new Producto("Vestido", 25500.00);
        Producto producto7 = new Producto("Pollera", 15000.00);
        Producto producto8 = new Producto("Bufanda", 9000.00);
        Producto producto9 = new Producto("Corbata", 6000.00);
        Producto producto10 = new Producto("Guantes", 3000.00);
        
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        
        orden2.mostrarOrden();

        Orden orden3 = new Orden();
        Producto producto11 = new Producto("Collar", 30000.00);
        orden3.agregarProducto(producto11);
        orden3.mostrarOrden();
    }
}
