/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar cuantos
             numeros se han introducido. Hacer con clase Scanner y luego con 
             JOoptionPane
 */
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero >= 0){
            System.out.println("El numero "+numero+" es POSITIVO.");
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
        System.out.println("A ingrasado "+conteo+" numeros que no son negativos.");
    }
}
