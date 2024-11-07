package ar.com.codesystem.ventas;

public class Producto {
    // Atributos
    private int idProducto;
    private String nombre;
    private double precio;
    private static int contadorProductos;

    //Constructor vacio
    private Producto() {
        this.idProducto = ++Producto.contadorProductos;
    }

    public Producto(String nombre, double precio) {
        this();
        this.nombre = nombre;
        this.precio = precio;
    }

    public int getIdProducto() {
        return idProducto;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override // Sobreescribimos el toString() para mostrar la cadena de producto
    public String toString() {
        return "Producto { " + "idProducto: " + idProducto + ", nombre: " + nombre + ", precio: " + precio + " }";
    }
}