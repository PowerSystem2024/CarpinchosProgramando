
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        // TAREA: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        // e imprimir, luego modificar sus valores y volver a imprimir.
        
        // Crear el segundo objeto de tipo Persona con valores iniciales
        Persona persona2 = new Persona("María", 65000, true);
        System.out.println("persona2 con su nombre inicial: "+persona2.getNombre());
        System.out.println("persona2 con su sueldo inicial: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano inicial: "+persona2.isEliminado());
        
        // Modificar valores de persona2
        persona2.setNombre("Ana");
        persona2.setSueldo(70000);
        persona2.setEliminado(false);
        
        //Imprimier los valores modificados de persona2
        System.out.println("persona2 con su nombre modificado: "+persona2.getNombre());
        System.out.println("persona2 con su sueldo modificado: "+persona2.getSueldo());
        System.out.println("persona2 booleano modificado: "+persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1); // llama automaticamente al toSting
        System.out.println("persona1: "+persona1.toString());
    }
}
