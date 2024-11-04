
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        // Método especial
        Persona persona1 = new Persona();
        /* Constructor - Método especial donde reserva memoria para crear objetos.
                     - Al crear el objeto, le regresa las referencias donde se creo el objeto 
                       y se la asigna a la variable
                     - Permite asignar valores al objeto desde su creación.
         Al colocar los () se transforma en conductor.
         Gracias a esto, 'persona1' se transformó en objeto.*/
        
        // El valor hexadecimal normalmente comienza con 0x
        persona1.nombre = "Ana";
        persona1.apellido = "Ríos";
        persona1.obtenerInformacion();
        System.out.println("persona1 = " + persona1);
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        persona2.obtenerInformacion();
        persona2.nombre = "Lucas";
        persona2.apellido = "Cerbino";
        persona2.obtenerInformacion();
        
    }
}
