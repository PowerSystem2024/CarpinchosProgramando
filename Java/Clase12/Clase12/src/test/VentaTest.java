package test;
  /*
        Tarea:
        Crear mas objetos del tipo Producto.
        Crear mas objetos del tipo Orden.
        */

import ar.com.codesystem.ventas.*;

public class VentaTest {

    public static void main(String[] args) {

        Producto producto1 = new Producto("Pantalon", 9500);
        Producto producto2 = new Producto("Campera", 29900);
        Producto producto3 = new Producto("Camisa", 9900);
        Producto producto4 = new Producto("Zapatillas", 30000);
        Producto producto5 = new Producto("Buzo", 10000);
        Producto producto6 = new Producto("Short", 8000);
        Producto producto7 = new Producto("Medias deportivas", 7900);
        Producto producto8 = new Producto("Saco", 15000);
        Producto producto9 = new Producto("Bermuda", 9800);
        Producto producto10 = new Producto("Sweater", 16000);
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();

        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto10);
        orden1.agregarProducto(producto8);
        orden1.agregarProducto(producto6);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto1);
        orden2.agregarProducto(producto9);
        orden1.mostrarOrden();
        System.out.println("   ---------   \n");
        orden2.mostrarOrden();


    }
}