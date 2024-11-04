// Pedir un numero con Scanner y Mostrar los numeros desde 1 hasta N
package clase5;

import java.util.Scanner;

public class MostrarNroHastaNScanner {

    public static void main(String[] args) {
      
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Por favor, ingrese un número: ");
        int numero = entrada.nextInt();
        
        System.out.println("Los números desde 1 hasta " + numero + " son:");
        for (int i = 1; i <= numero; i ++) {
            System.out.println(i);
        }        
    }
 }