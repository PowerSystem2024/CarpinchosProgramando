
package Clases;

public class Persona {
    // Atributos de la clase (Características)
    // Para que estos atributos sean llamados, es necesario especificar que son públicos
    public String nombre;
    public String apellido;
    
    // Métodos de la clase (Acciones)
    public void obtenerInformacion(){
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido: " + apellido);
        
    }
}
