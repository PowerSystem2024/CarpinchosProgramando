

package Persona;

public class PruebaPersona {
    public static void main(String[] args) {
        // Crear una instancia de la clase Persona
        Persona persona1 = new Persona();

        // Asignar valores a los atributos
        persona1.nombre = "Juan";
        persona1.apellido = "Pérez";

        // Mostrar la información de la persona
        persona1.obtenerInformacion();

        // Modificar los atributos de la persona
        persona1.nombre = "María";
        persona1.apellido = "López";

        // Mostrar la información actualizada de la persona
        persona1.obtenerInformacion();
    }
}