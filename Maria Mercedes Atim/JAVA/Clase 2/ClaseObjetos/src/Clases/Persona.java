package Clases;

public class Persona{
    
    // Encapsulamiento: es una forma de proteger los datos y hacer que el código sea más fácil de mantener y entender. 
    // Es una forma de esconder los detalles internos de un objeto y solo exponer lo necesario para que otros objetos puedan interactuar con él.-
    // Para ocultar estos datos, los hacemos "private". Esto significa que solo el propio objeto puede acceder y modificar estos datos directamente.-
    // "Default" (o paquete): Accesible solo dentro del mismo paquete. Si no se especifica un modificador de acceso, se usa el modificador de acceso por defecto.-
    // Protected: Accesible dentro del mismo paquete y por subclases, incluso si están en paquetes diferentes. Para permitir que las subclases 
    // (herederos) accedan a los miembros de la clase base, y también para permitir el acceso a otras clases en el mismo paquete.-
    // Public: Accesible desde cualquier lugar, es decir, desde cualquier clase en cualquier paquete. 
    // Para hacer que las clases, métodos o atributos estén disponibles globalmente.-
    
   String nombre;
   String apellido;
   int dni;
   String eMail;
   String telefono;
   
   // Si necesitas que otros objetos puedan leer o modificar estos datos, proporcionas métodos públicos 
   // (llamados métodos de acceso o getters y setters) para acceder a ellos.
   // Los getters permiten que otros objetos lean los datos.
   // Los setters permiten que otros objetos modifiquen los datos, pero con control.

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public int getDni() {
        return dni;
    }

    public void setDni(int dni) {
        this.dni = dni;
    }

    public String geteMail() {
        return eMail;
    }

    public void seteMail(String eMail) {
        this.eMail = eMail;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + ", dni=" + dni + ", eMail=" + eMail + ", telefono=" + telefono + '}';
    }
    
   
}