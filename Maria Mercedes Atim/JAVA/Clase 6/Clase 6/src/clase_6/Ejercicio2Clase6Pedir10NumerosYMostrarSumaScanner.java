// Pedir 10 Numeros y escribir la suma total - Clase Scanner

package clase_6;

import java.util.Scanner;

public class Ejercicio2Clase6Pedir10NumerosYMostrarSumaScanner {

    public static void main(String[] args) {
        int numero, iterador, suma = 0;

        Scanner entrada = new Scanner(System.in);

        for (iterador = 0; iterador < 10; iterador++) {
            System.out.println("Ingrese un número: ");
            numero = entrada.nextInt();
            suma += numero;
        }
        System.out.println("La suma de los numeros ingresados es: " + suma);
    }
}