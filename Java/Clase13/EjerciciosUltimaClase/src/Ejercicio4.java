
import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];
   
        System.out.println("Introduce 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            tabla[i] = scanner.nextInt();
        }

        int posicion;
        do {
            System.out.print("Introduce la posición a eliminar (entre 0 y 9): ");
            posicion = scanner.nextInt();
        } while (posicion < 0 || posicion > 9);
 
        for (int i = posicion; i < tabla.length - 1; i++) {
            tabla[i] = tabla[i + 1];
        }
   
        System.out.println("\nTabla después de eliminar el elemento en la posición " + posicion + ":");
        for (int i = 0; i < tabla.length - 1; i++) {
            System.out.print(tabla[i] + " ");
        }

        scanner.close();
    }
}
