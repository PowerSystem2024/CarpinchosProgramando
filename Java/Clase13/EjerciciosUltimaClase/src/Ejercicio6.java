
import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arreglo1 = new int[10];
        int[] arreglo2 = new int[10];
        int[] arregloFusionado = new int[20];

        System.out.println("Introduce 10 números enteros para el primer arreglo en orden creciente:");
        for (int i = 0; i < 10; i++) {
            arreglo1[i] = scanner.nextInt();
            if (i > 0 && arreglo1[i] < arreglo1[i - 1]) {
                System.out.println("Los números deben estar en orden creciente.");
                i--; 
            }
        }
        System.out.println("Introduce 10 números enteros para el segundo arreglo en orden creciente:");
        for (int i = 0; i < 10; i++) {
            arreglo2[i] = scanner.nextInt();
            if (i > 0 && arreglo2[i] < arreglo2[i - 1]) {
                System.out.println("Los números deben estar en orden creciente.");
                i--; 
            }
        }

        int i = 0, j = 0, k = 0;
        while (i < 10 && j < 10) {
            if (arreglo1[i] < arreglo2[j]) {
                arregloFusionado[k++] = arreglo1[i++];
            } else {
                arregloFusionado[k++] = arreglo2[j++];
            }
        }

        while (i < 10) {
            arregloFusionado[k++] = arreglo1[i++];
        }

        while (j < 10) {
            arregloFusionado[k++] = arreglo2[j++];
        }

        System.out.println("\nArreglo fusionado en orden creciente:");
        for (int elemento : arregloFusionado) {
            System.out.print(elemento + " ");
        }
        scanner.close();
    }
}
