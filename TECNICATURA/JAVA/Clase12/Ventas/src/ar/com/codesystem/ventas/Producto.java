
package ar.com.codesystem.ventas;

public class Producto {
    // Atributos de la clase
    private int idProducto;
    private String nombre;
    private double precio;
    private static int contadorProductos;
    
    // 1. Constructor vacío
    private Producto(){
        this.idProducto = ++ Producto.contadorProductos;
    }
    
    // 2. Constructor con parámetros
    public Producto(String nombre, double precio){
        // Llamado al constructor vacío para el aumento del idProducto
        this();
        this.nombre = nombre;
        this.precio = precio;
    }

    // Métodos Getter y Setter
    // Método Getter (Único caso) para 'idProducto'
    public int getIdProducto() {
        return idProducto;
    }

    // Métodos Getter y Setter para 'nombre'
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // Métodos Getter y Setter para 'precio'
    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    // Métodos Getter y Setter para 'ContadorProductos'
    public static int getContadorProductos() {
        return contadorProductos;
    }

    public static void setContadorProductos(int contadorProductos) {
        Producto.contadorProductos = contadorProductos;
    }
    
    // Método toString
    @Override
    public String toString() {
        return "Producto{" + "idProducto = " + idProducto + ", nombre = " + nombre + ", precio = " + precio + '}';
    }
}
