/*
Uso de la palabra FINAL:
Tiene diferentes significados, depende de donde se aplique:
Variables: Evita cambiar el valor que almacena la variable.
Métodos: Evita que se modifique la definicion o el comportamiento de un metodo desde una subclase hija.
Clases: Evita que se creen clases hijas.

Otra Caracteristica es que cuando trabajamos con variables se combina con el modificador de acceso estático 
para convertir una variable en una constante, es decir, no se puede modificar su valor. Un ejemplo de esto es 
la clase Math en la que todos sus atributos son de tipo static y final, es por eso que la variable PI* se conoce 
como una constante
 */
package test;

import domain.Persona;

public class TestFinal {
    
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        //miDni = 20312321; No se puede modificar
        //Persona.CONSTANTE_AQUI = 9; No se puede modificar porque es final
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        // persona1 = new Persona(); No se puede asignar una nueva referencia.
        persona1.setNombre("Mercedes Atim");
        System.out.println(persona1.getNombre() + " es el nombre de persona1");
        persona1.setNombre("Mariana Aguilera");
        System.out.println(persona1.getNombre() + " es el nombre de persona1");
    }
}