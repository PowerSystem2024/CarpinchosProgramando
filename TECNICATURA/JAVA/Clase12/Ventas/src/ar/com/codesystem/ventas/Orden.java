
package ar.com.codesystem.ventas;

public class Orden {
    // Atributos de la clase
    private int idOrden;
    // Declaración del arreglo
    private Producto productos[];
    private static int contadorOrdenes;
    private int contadorProductos;
    // Declaración de la constante
    private static final int MAX_PRODUCTOS = 10;
    
    // Constructor vacío
    public Orden(){
        this.idOrden = ++ Orden.contadorOrdenes;
        // Declaración de límites de productos
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    // Método que combina la clase Orden y la clase Objeto
    public void agregarProducto(Producto producto){
        // Condicional para comprobaciones
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){
            this.productos[contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ha superado el máximo de productos: " + Orden.MAX_PRODUCTOS);
        }
    }
    
    // Creación de método
    public double calcularTotal(){
        // Variable temporal
        double total = 0;
        // Ciclo for
        for (int i = 0; i < this.contadorProductos; i++) {
            // Producto producto = this.productos[i];
            // total += producto.getPrecio();
            // Línea de código -> Junta las dos líneas de códigos anteriores
            //                    en una sola
            total += this.productos[i].getPrecio();
        }
        return total;
    }
  
    // Creación de método
    public void mostrarOrden(){
        System.out.println("ID Orden: " + idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("El total de la orden es: $" + totalOrden);
        System.out.println("Productos de la orden: ");
        // Ciclo for
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
        }
    }
}
