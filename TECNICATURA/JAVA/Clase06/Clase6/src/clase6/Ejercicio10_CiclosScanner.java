/*
Ejercicio 10: Ciclos - Clase Scanner y Clase JOptionPane
    Pedir 10 números y escribir la suma total.
*/

package clase6;
import java.util.Scanner;

public class Ejercicio10_CiclosScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int sumaTotal = 0;
        
        for (int i = 1; i < 11; i++) {
            System.out.print("Ingrese el número " + i + ": ");
            int numero = scanner.nextInt();  
            sumaTotal += numero;  
        }
        System.out.println("La suma total de los 10 números es: " + sumaTotal);
    }
}
