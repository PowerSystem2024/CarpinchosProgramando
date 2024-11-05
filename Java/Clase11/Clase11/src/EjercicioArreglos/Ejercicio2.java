/*Ejercicio 2:
Leer 5 numeros, guardarlos en un arreglo y mostrarlos en el orden inverso al introducido*/
package EjercicioArreglos;

import java.util.Scanner;

public class Ejercicio2 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada del usuario

        System.out.println("Por favor ingrese 5 numeros: "); // Pedimos al usuario que ingrese 5 n�meros
        int numeros[] = new int[5]; // Creamos un arreglo para almacenar 5 n�meros

        // Bucle para leer 5 n�meros y almacenarlos en el arreglo
        for (int i = 0; i < numeros.length; i++) { // Itera 5 veces
            System.out.print("Numero " + (i + 1) + ": "); // Pide el n�mero correspondiente
            numeros[i] = entrada.nextInt(); // Lee el n�mero y lo guarda en el arreglo
        }

        System.out.println("Mostramos los n�meros en orden inverso: "); // Mensaje para indicar que se mostrar�n los n�meros

        // Bucle para mostrar los n�meros en orden inverso
        for (int i = numeros.length - 1; i >= 0; i--) { // Itera desde el �ltimo �ndice hasta el primero
            System.out.println(numeros[i]); // Imprime cada n�mero en orden inverso
        }
    }
}