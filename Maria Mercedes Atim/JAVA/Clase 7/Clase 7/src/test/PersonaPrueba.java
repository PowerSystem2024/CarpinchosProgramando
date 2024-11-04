package test;

import dominio.*;

public class PersonaPrueba {

    public static void main(String[] args) {

        Persona persona1 = new Persona("Mariana", 200000, false);

        System.out.println("El nombre de persona1 es: " + persona1.getNombre());
        System.out.println("persona1 = " + persona1);

        // Modificar a traves de los metodos:
        persona1.setNombre("Wanda Oriana");

        // persona1.nombre = "Wanda Oriana"; No se puede modificar un atributo privado.
        // System.out.println("Nombre es: " + persona1.nombre); No se puede mostrar de esta manera un atributo privado.
        System.out.println("Ya modificado, el nombre de persona1 es: " + persona1.getNombre());

        System.out.println("El sueldo de persona1 es: " + persona1.getSueldo());
        System.out.println("El resultado booleano para persona1 es: " + persona1.isEliminado());

        System.out.println("""
                           \nTAREA:
                           Crear otro objeto de tipo Persona. Asignar valores de forma inicial, imprimirlos.
                           Luego modificarlos e imprimir nuevamente.
                           """);

        Persona persona2 = new Persona("Nicolas Mercado", 3000000, false);
        // Mostramos los datos iniciales: 
        System.out.println("El nombre de persona2 es: " + persona2.getNombre());
        System.out.println("El sueldo de persona2 es: " + persona2.getSueldo());
        System.out.println("El resultado booleano de persona2 es: " + persona2.isEliminado());

        // Modificamos los datos:
        persona2.setNombre("Nelson Rios");
        persona2.setSueldo(4000000);

        // Mostramos los datos modificados: 
        System.out.println("\nEl nombre modificado de persona2 es: " + persona2.getNombre());
        System.out.println("El sueldo modificado de persona2 es: " + persona2.getSueldo());
        
        // Metodo toString()
        System.out.println("\nMostramos persona con Metodo toString()");
        System.out.println("persona1: " + persona1.toString());
        System.out.println("persona1: " + persona2.toString());        
    }
}