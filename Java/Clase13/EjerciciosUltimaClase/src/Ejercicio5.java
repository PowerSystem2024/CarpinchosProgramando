
import java.util.Scanner;

public class Ejercicio5 {

     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tablaOriginal = new int[10];
        int[] tablaSeparada = new int[10];

        System.out.println("Introduce 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            tablaOriginal[i] = scanner.nextInt();
        }

        int indicePares = 0;
        int indiceImpares = 0;

        for (int i = 0; i < 10; i++) {
            if (tablaOriginal[i] % 2 == 0) {
                tablaSeparada[indicePares++] = tablaOriginal[i];
            }
        }

        indiceImpares = indicePares; 
        for (int i = 0; i < 10; i++) {
            if (tablaOriginal[i] % 2 != 0) {
                tablaSeparada[indiceImpares++] = tablaOriginal[i];
            }
        }

        System.out.println("\nTabla original:");
        for (int i = 0; i < 10; i++) {
            System.out.print(tablaOriginal[i] + " ");
        }

        System.out.println("\n\nTabla con pares e impares separados:");
        for (int i = 0; i < 10; i++) {
            System.out.print(tablaSeparada[i] + " ");
        }

        scanner.close();
    }
}
