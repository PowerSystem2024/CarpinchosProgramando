package Clase03;


import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {

        int numero, numeroAAdivinar, contador =0;
        Scanner entrada = new Scanner(System.in);

        numeroAAdivinar = (int) (Math.random() * 101);

        do {
            System.out.println("Usted debe adivinar un número de 0 a 100. Ingrese un numero y se le indicará si adivinó, si es mayor o menor.");
            numero = entrada.nextInt();
            contador++;

            if (numero < numeroAAdivinar) {
                System.out.println("El número es mayor.");
            } else if (numero > numeroAAdivinar) {
                System.out.println("El número es menor.");
            } else {
                System.out.println("¡Felicidades! Usted adivinó el número :)");
            }
        } while (numero != numeroAAdivinar);
        System.out.println("Usted adivinó el número tras " + contador + " intentos.");
    }

}