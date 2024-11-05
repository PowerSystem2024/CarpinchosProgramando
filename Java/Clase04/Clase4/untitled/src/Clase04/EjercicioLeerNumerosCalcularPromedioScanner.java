
// Solicitar el ingreso de numeros hasta que se introduzca uno negativo y calcular la media.
// Realizamos el ejercicio con Scanner
package Clase04;

import java.util.Scanner;

public class EjercicioLeerNumerosCalcularPromedioScanner {

    public static void main(String[] args) {
        int numero, suma = 0, contador = 0;

        Scanner entrada = new Scanner(System.in);

        do {
            System.out.println("Ingrese un número. Para salir ingrese un número negativo.");
            numero = entrada.nextInt();
            if (numero >= 0) {
                suma += numero;
                contador++;
            }
        } while (numero >= 0);
        double promedio = (double) suma / contador;
        System.out.println("Se ingresó un número negativo, finalizó el programa. \nEl promedio de los números ingresados es: " + promedio);
    }
}