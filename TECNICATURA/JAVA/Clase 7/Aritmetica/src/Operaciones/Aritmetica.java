// Atributos y metodos comienzan con minusculas, para diferenciarlos con las clases que empiezan con mayusculas.

package Operaciones;

public class Aritmetica {        // Para la clase usamos nomenclatura 'PascalCase'
    // Atributos de la clase
    int a;
    int b;
    
    //----- SOBRECARGA DE CONSTRUCTORES ----
    // El constructor es un metodo especial
    public Aritmetica(){  // constructor 1 (vacio). Se crea por defecto
        System.out.println("Se esta ejecutando el constructor n° 1");
    }
    
    public Aritmetica(int a, int b){ // constructor 2 ( si creo un constructor, el constructor 1 que se creaba por defecto, debo crearlo si o si porque ya no se creara automaticamente.
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor n° 2");
    }
    // ---------------------------------------
    
    // Metodo
    public void sumarNumeros(){  // Para metodos y atributos usamos nomenclatura 'camelCase'
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    // Metodo 2
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
    }
    
    // Metodo 3
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1; // El argumento 'a' se asigna al atributo this.a
        this.b = arg2;
       // return a + b;
       return sumarConRetorno();  // retorna otro metodo (el 2) | Esto solo se hace dentro de la misma clase
    }
}
