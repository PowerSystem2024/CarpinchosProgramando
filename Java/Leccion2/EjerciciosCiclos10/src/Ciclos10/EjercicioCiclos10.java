package Ciclos10;


import java.util.Scanner;

public class EjercicioCiclos10 {
    public static void main(String[] args) {
        /*
        EJERCICIO 10: Pedir 10 numeros y escribir la SUMA
        */
        Scanner scan = new Scanner(System.in);
        int sum = 0;

        for (int i = 0; i< 10;i++) {
            System.out.print("Ingrese un numero: ");
            sum += scan.nextInt();

        }
        System.out.println("La suma es: " + sum);

    }

}