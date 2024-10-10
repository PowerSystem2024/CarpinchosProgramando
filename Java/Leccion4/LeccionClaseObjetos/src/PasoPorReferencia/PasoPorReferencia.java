package PasoPorReferencia;

import Persona.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("Nombre de la persona = " + persona1.nombre);

        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: " + persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = null;
        persona2  = cambiarElValor(persona2);
        System.out.println("El nuevo valor del objeto es: "+persona2.nombre);

    }

    public static void cambiarValor(Persona persona) {
        // Paso por referencia
        persona.nombre = "Maria";
    }


    public static Persona cambiarElValor(Persona persona) {
        if (persona == null) {
            System.out.println("Valor de persona es invalido :NULL");
            return null;
        } else {


            persona.nombre = "Monica";
            return persona;
        }
    }

}