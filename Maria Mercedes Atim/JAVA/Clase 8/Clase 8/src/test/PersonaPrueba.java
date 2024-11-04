package test;

import domain.Persona;

public class PersonaPrueba {
    private int contador;

    public static void main(String[] args) {
        // No se puede ejecutar metodos que no sean estaticos en un contexto estático
        // La palabra this no puede ser referenciada dentro de un contexto estático
        Persona persona1 = new Persona("Melina");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Ana Paula");
        System.out.println("persona2 = " + persona2); //El id se incrementa por el atributo estático
        imprimir(persona1);
        // this.contador = 10; No se puede referenciar this en este metodo estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }

    public static void imprimir(Persona persona) { // Este metodo no es estático
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("Mariana")); // Se crea un objeto para que pase de forma dinánica
        return this.contador;
    }
}
