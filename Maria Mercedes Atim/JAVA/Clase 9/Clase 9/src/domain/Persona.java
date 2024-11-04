/*PUBLIC: Los miembros (atributos y métodos) declarados como public son accesibles desde
cualquier otra clase en cualquier paquete. No hay restricciones.
PRIVATE: Los miembros declarados como private son accesibles solo dentro de la propia clase. 
No pueden ser accedidos desde otras clases, ni siquiera si están en la misma jerarquía de herencia.
PROTECTED: Los miembros declarados como protected son accesibles dentro de la propia clase, 
en clases del mismo paquete y en clases que heredan de la clase (incluso si están en un paquete diferente). 
Esto permite un mayor acceso que private, pero menos que public.
-public: Acceso total (todos).
-private: Acceso restringido (solo dentro de la clase).
-protected: Acceso intermedio (dentro de la clase, mismo paquete, y subclases).
*/
package domain;

// Clase que representa una persona
public class Persona {
    // Atributos de la clase encapsulados con protected, accesibles por las clases que heredan
    protected String nombre;   // Nombre de la persona
    protected char genero;     // Género de la persona (por ejemplo, 'M' o 'F')
    protected int edad;        // Edad de la persona
    protected String direccion; // Dirección de la persona

    // Constructor vacío que permite crear un objeto sin inicializar los atributos
    public Persona() { 
    }

    // Constructor que recibe solo el nombre
    public Persona(String nombre) {
        this.nombre = nombre; // Inicializa el nombre con el valor proporcionado
    }
    
    // Constructor que recibe todos los atributos
    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;     // Inicializa el nombre
        this.genero = genero;     // Inicializa el género
        this.edad = edad;         // Inicializa la edad
        this.direccion = direccion; // Inicializa la dirección
    }

    // Método para obtener el nombre de la persona
    public String getNombre() {
        return this.nombre; // Retorna el nombre
    }

    // Método para establecer un nuevo nombre
    public void setNombre(String nombre) {
        this.nombre = nombre; // Asigna el nuevo nombre
    }

    // Método para obtener el género de la persona
    public char getGenero() {
        return this.genero; // Retorna el género
    }

    // Método para establecer un nuevo género
    public void setGenero(char genero) {
        this.genero = genero; // Asigna el nuevo género
    }

    // Método para obtener la edad de la persona
    public int getEdad() {
        return this.edad; // Retorna la edad
    }

    // Método para establecer una nueva edad
    public void setEdad(int edad) {
        this.edad = edad; // Asigna la nueva edad
    }

    // Método para obtener la dirección de la persona
    public String getDireccion() {
        return this.direccion; // Retorna la dirección
    }

    // Método para establecer una nueva dirección
    public void setDireccion(String direccion) {
        this.direccion = direccion; // Asigna la nueva dirección
    }
    
    // Método que devuelve una representación en forma de cadena del objeto Persona
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(); // Crea un nuevo StringBuilder para construir la cadena
        sb.append("Persona "); // Agrega el texto "Persona"
        sb.append("nombre: ").append(nombre); // Agrega el nombre
        sb.append("\ngenero: ").append(genero); // Agrega el género
        sb.append("\nedad: ").append(edad); // Agrega la edad
        sb.append("\ndireccion: ").append(direccion); // Agrega la dirección
        return sb.toString(); // Retorna la cadena completa
    }   
}