package Clase03;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int numero, contador = 0;

        do {
            System.out.println("Ingrese un número. Para finalizar, ingrese un numero negativo.");
            numero = entrada.nextInt();
            if (numero >= 0) {
                contador++;
            }
        } while (numero >= 0);
        System.out.println("Se ingresó un numero negativo. El programa finalizó.");
        System.out.println("Se ingresaron: " + contador + " números.");
    }
}
