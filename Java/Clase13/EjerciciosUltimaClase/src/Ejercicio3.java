
import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];
        int numElementos = 5; 
        
        System.out.println("Introduce 5 números enteros en orden creciente:");
        for (int i = 0; i < numElementos; i++) {
            tabla[i] = scanner.nextInt();
            if (i > 0 && tabla[i] < tabla[i - 1]) {
                System.out.println("Los números deben estar en orden creciente.");
                i--; // Volvemos a pedir el número en la misma posición
            }
        }
        System.out.print("Introduce el número a insertar: ");
        int n = scanner.nextInt();
        
        int pos = numElementos; 
        for (int i = 0; i < numElementos; i++) {
            if (n < tabla[i]) {
                pos = i;
                break;
            }
        }

        for (int i = numElementos; i > pos; i--) {
            tabla[i] = tabla[i - 1];
        }

        tabla[pos] = n;
        numElementos++; 

        System.out.println("\nTabla después de insertar el número " + n + ":");
        for (int i = 0; i < numElementos; i++) {
            System.out.print(tabla[i] + " ");
        }

        scanner.close();
    }
}
