package Operaciones;


public class PruebaAritmetica{

    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica(); // Instancia nuevo objeto Aritmetica
        aritmetica1.a = 3; // Asignamos valor al atributo a
        aritmetica1.b = 7; // Asignamos valor al atributo b
        aritmetica1.sumarNumeros(); // Invocamos el metodo void de la clase
        System.out.println(aritmetica1.sumarConRetorno()); //este metodo va a retornar
        //un entero, en este caso 10 que es el resultado de la suma
        System.out.println(aritmetica1.sumarConArgumentos(12, 26));
    }
}