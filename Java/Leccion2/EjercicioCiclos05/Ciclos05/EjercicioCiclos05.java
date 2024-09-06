
/* Ejercicio 5_: Realizar un juego para adivinar un numero
para ello generar un numero aleatorio entre 0-100, y lugo
ir pidiendo numeros indicando " es mayor" o " es menor", segun sea mayor o menor
con respecto al Numero N.
El proceso termina cuando el usuario acierta , y mosgtramos el numero de intentos hechos.*/



package Ciclos05;

import java.util.Scanner;


public class EjercicioCiclos05 {




    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int numero, aleatorio, conteo = 0; // Genera un número aleatorio entre 0 y 100
        aleatorio = (int) (Math.random() * 100);

        System.out.println("Bienvenido al juego de adivinar el numero");
        System.out.println("Intenta adivinar el numero secreto entre 0 y 100, con la menor cantidad de intentos.");

        do {
            System.out.print("Ingresa tu numero: ");
            numero = Integer.parseInt(entrada.nextLine());

            if (numero < aleatorio) {
                System.out.println("El numero ** SECRETO ** es mayor");
            } else if (numero > aleatorio) {
                System.out.println("El numero **SECRETO** es menor.");
            } else {
                System.out.println("Felicidades has adivinado el numero");

            }
            conteo++;
        } while (numero != aleatorio);
        System.out.println("Adivinaste el numero en :" + conteo + " intentos");
    }
}