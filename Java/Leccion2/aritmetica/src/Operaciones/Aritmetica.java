package Operaciones;

public class Aritmetica{
    // Atributos de la clase

    int a, b;

    // Constructor es un metodo especial. Cumple 3 funciones importantes:
    // • Nos sirve para crear el objeto
    // • Reserva un espacio en memoria
    // • Sirve para inicializar los atributos de la clase

    public Aritmetica() { // El constructor vacio se crea por defecto.
        System.out.println("Se está  ejecutando el constructor N° 1");
    }

    // Sobrecarga de metodos: La sobrecarga de métodos es cuando se tiene
    // varios métodos en un programa que tienen el mismo nombre, pero hacen cosas diferentes.
    // Se diferencian por la cantidad o el tipo de información que reciben (parámetros).

    public Aritmetica(int a, int b) { // No se crea por defecto
        this.a = a;
        this.b = b;
        System.out.println("\nSe esta ejecutando el constructor N° 2");
    }

    // Metodos

    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println("\nMetodo VOID: resultado = " + resultado);  // Enviar información a la consola NO es lo mismo que retornar un valor.
    }

    public int sumarConRetorno(){ //Retorna un valor entero
        int resultado = a + b;
        return resultado;
    }

    public int sumarConArgumentos(int arg1,  int arg2){
        this.a = arg1; // El argumento "a" se asigna el atributo this.a
        this.b = arg2; // El uso del this en este caso es opcional
        //return a + b;
        return sumarConRetorno();
    }
}