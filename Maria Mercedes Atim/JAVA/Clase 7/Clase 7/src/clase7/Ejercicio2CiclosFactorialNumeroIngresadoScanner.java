// Pedir un numero y calcular su factorial. Hacerlo con Scanner
package clase7;

import java.util.Scanner;

public class Ejercicio2CiclosFactorialNumeroIngresadoScanner {

    public static void main(String[] args) {

        int numero;
        long factorial = 1; // Iniciamos factorial en 1 y como long ya que es un numero que va creciendo rapidamente.

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un numero para calcular su factorial: ");

        numero = entrada.nextInt();

        for (int i = 1; i <= numero; i++) { //Iniciamos el iterador en 1. iterará hasta el numero que ingresó el usuario y avanzará de 1 en 1
            factorial *= i; // Multiplicamos el resultado de la multiplicacion de los numeros y lo guardamos en factorial.
        }
        System.out.println("El factorial de " + numero + "! es: " + factorial);
    }
}