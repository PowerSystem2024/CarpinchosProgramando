// Leer numeros hasta que se introduzca un cero. Para cada uno, identificar si es par o impar.
// Primero lo haremos con la clase Scanner
package Clase03;

import java.util.Scanner;

public class Ejercicio1 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int numero;

        do {
            System.out.print("Ingrese un número para verificar si es PAR o IMPAR (0 para salir): ");
            numero = entrada.nextInt(); // guardamos en numero, lo que el usuario ingrese por teclado.

            if (numero != 0) {
                if (numero % 2 == 0) {
                    System.out.println("El número " + numero + " es PAR.");
                } else {
                    System.out.println("El número " + numero + " es IMPAR.");
                }
            } else {
                System.out.println("El sistema se detuvo porque se ingresó cero (0).");
            }
        } while (numero != 0);
    }
}