package Ciclos05;
import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero_aleatorio;
        int numero;
        int contador = 0;

        numero_aleatorio = (int)(Math.random() * 100); // Esto genera un número aleatorio
        do {
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero > numero_aleatorio) {
                System.out.println("Digite un número menor");
            } else if (numero < numero_aleatorio) {
                System.out.println("Digite un número mayor");
            } else {
                System.out.println("¡¡¡FELICIDADES!!! Has adivinado el número");
            }
            contador++;
        } while (numero != numero_aleatorio);
        System.out.println("Adivinaste el número en: " + contador + " intentos");
    }
}
