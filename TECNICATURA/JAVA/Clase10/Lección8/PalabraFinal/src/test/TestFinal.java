// Uso de la palabra Final
//Esta palabra tiene diferentes significados dependiendo de donde se aplique:
//   variables: Evita cambiar el valor que almacena la variable
//   métodos: Evita que se modifique la definición o el comportamientode un método desde una subclase(hija)
//   clases: Evita que se creen clases hijas
// Otra característica es que normalmente, cuando trabajamos con variables se combina con el modificador de 
//accceso estático para convertir una variable en una constante, es decir que no se puede modificar su valor,
//el ejemplo de ésto es la clase Math en la cual todos sus atributos son de tipo Static y final, es por éso que 
//la variable pi* se conoce como una constante.
package test;

import domain.Persona;

public class TestFinal {

    public static void main(String[] args) {
        final int miDni = 33344339;
        System.out.println("miDni = " + miDni);
        // miDni = 44333865; No se puede asignar un valor porque es final(es constante)
        //Persona.CONSTANTE_AQUI = 9; // No se puede modificar
        System.out.println("Mi atributo Cte es: " + Persona.CONSTANTE_AQUI);

        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Nelson R: ");
        System.out.println("persona1 nombre: " + persona1.getNombre());
        persona1.setNombre("Analía");//No se puede hacer una nueva referencia, pero sí modificar el valor del atributo
        System.out.println("persona1 nombre: " + persona1.getNombre());
    }

}
