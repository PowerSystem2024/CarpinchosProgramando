
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10;  // variables locales
        int b = 7;      // Memoria stack
        miMetodo(); // Llamamos el metodo nuevo
        
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3 ;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = "+resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12 , 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = "+aritmetica2.a);
        System.out.println("aritmetica2 = "+aritmetica2.b);
        
        // aritmetica1 = null;   Nunca utilizar esto
        // System.gc();   Metodo para limpiar residuos, es PESADO, no utilizar.
        
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }
    
// El alcance de un atributo es superior al de una variable local
//    variables locales --> Memoria stack
//    objetos o atributos --> Memoria heap
    
    // Modularidad | creamos un nuevo metodo
    // Otro metodo
    public static void  miMetodo(){
        // a = 10;  // Una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }
}

// Solo puede haber una clase publica
// Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){  // constructor
        super(); //Llamada al constructor de la clase Padre object
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); // el constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this: "+this);
    }
}
