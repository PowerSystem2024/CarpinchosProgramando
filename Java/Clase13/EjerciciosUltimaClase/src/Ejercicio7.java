
import java.util.Scanner;

public class Ejercicio7 {

 public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arreglo = new int[10];

        System.out.println("Introduce 10 números enteros en orden creciente:");
        for (int i = 0; i < 10; i++) {
            arreglo[i] = scanner.nextInt();
            if (i > 0 && arreglo[i] < arreglo[i - 1]) {
                System.out.println("Los números deben estar en orden creciente.");
                i--; 
            }
        }

        System.out.print("Introduce el número a buscar (N): ");
        int n = scanner.nextInt();

        int posicion = -1;
        for (int i = 0; i < 10; i++) {
            if (arreglo[i] == n) {
                posicion = i;
                break;
            }
        }

        if (posicion != -1) {
            System.out.println("El número " + n + " se encuentra en la posición: " + posicion);
        } else {
            System.out.println("El número " + n + " no se encuentra en el arreglo.");
        }

        scanner.close();
    }
}
