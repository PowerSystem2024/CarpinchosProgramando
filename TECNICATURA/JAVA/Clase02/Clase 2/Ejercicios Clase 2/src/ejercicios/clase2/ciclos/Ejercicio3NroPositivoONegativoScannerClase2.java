package ejercicios.clase2.ciclos;

import java.util.Scanner;

public class Ejercicio3NroPositivoONegativoScannerClase2 {

    public static void main(String[] args) {
        int numero;

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un numero para verificar si es positivo o negativo: ");
        numero = entrada.nextInt();

        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El número " + numero + " es positivo.");
            } else {
                System.out.println("El número " + numero + " es negativo.");
            }
            System.out.println("Ingrese otro numero para verificar si es positivo o negativo: ");
            numero = entrada.nextInt();
        }
        System.out.println("El programa se detuvo, se ingresó cero. ");

    }   
}