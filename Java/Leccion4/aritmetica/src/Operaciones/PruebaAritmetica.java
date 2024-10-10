package Operaciones;

public class PruebaAritmetica {

    public static void main(String[] args) {
        // Variables locales:
        int a = 10, b = 7;    // Se puede usar inferencia de datos. No asi en la declaracion de parámetros.
        // Los variables locales pertenecen a la memoria stack
        // El alcance de un atributo es superior al de una variable ya que están asociados a una clase y son accesibles desde sus métodos
        // mientras que las variables locales (o de instancia) suelen estar limitadas al bloque o método donde se definen.

        miMetodo(); // Invocamos al metodo que creamos fuera de Main
        Aritmetica aritmetica1 = new Aritmetica(); // Instancia nuevo objeto Aritmetica
        aritmetica1.a = 3; // Asignamos valor al atributo a
        aritmetica1.b = 7; // Asignamos valor al atributo b
        aritmetica1.sumarNumeros(); // Invocamos el metodo void de la clase
        System.out.println(aritmetica1.sumarConRetorno()); //este metodo va a retornar
        //un entero, en este caso 10 que es el resultado de la suma
        System.out.println("Resultado suma con Argumentos: "+aritmetica1.sumarConArgumentos(12, 26));
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8); // Para almacenar un objeto o los atributos se utiliza Memoria Heap
        System.out.println("aritmetica2 = " + " a: " + aritmetica2.a + " b: " + aritmetica2.b);

        // aritmetica1 = null; Nunca utilizar esto. No se debe hacer
        // System.gc(); Garbage Collector. Este metodo se usa para limpiar residuos. Es pesado, no utilizar.
        Persona persona = new Persona("Wanda", "Lanatta");
        System.out.println("\npersona = " + persona);
        System.out.println("Persona Nombre: " + persona.nombre);
        System.out.println("Persona Apellido: " + persona.apellido);
    }

    //Modularidad Creamos un nuevo método
    public static void miMetodo() { // Modularidad
        int a = 10;  // El alcance de variables es dentro de un metodo. Si las declaro en un metodo, no debe usarse en otro.
        // Se debe declarar otra variable para usar dentro de este metodo.
        System.out.println("Aqui esta el otro metodo: miMetodo().\n");
    }
}

// A esta clase se puede acceder solamente desde el mismo paquete.
class Persona { // Solo puede haber una sola clase publica por plantilla. Las clases que se creen despues tienen el identificador default/package

    String nombre;
    String apellido;

    Persona(String nombre, String apellido) { // Constructor
        super(); // Constructor de la superClase Object
        new Imprimir().Imprimir(this); // Instanciamos una nueva clase imprimir.
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("\nObjeto Persona el operador this: " + this);
    }
}

class Imprimir{

    public Imprimir() {
        super(); // El constructor de la clase padre Object, para reservar memoria.
    }

    public void Imprimir(Persona persona){
        System.out.println("\nPersona desde la clase imprimir: " + (persona));
        System.out.println("Impresion del objeto de la clase Imprimir actual (this): " + this);
    }
}