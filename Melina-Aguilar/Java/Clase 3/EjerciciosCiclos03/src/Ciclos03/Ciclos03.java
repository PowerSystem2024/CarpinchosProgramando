// Una clase es una plantilla, de la cual vamos a poder crear "objetos"
// Clase persona: tiene atributos y metodos
// La clase es un "molde" donde podemos crear uno o mas objetos.
// en objetos se define a la "persona"

/* 
Ejercicio 3: Leer numeros hasta que se introduzca un cero. 
            Para cada uno indicar si es par o impar.
            Primero lo haremos con la calse Scanner, luego con JoptionPane
*/
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        
        System.out.println("Digite un numero: " );
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El numero ingresado "+numero+" es PAR.");
            }
            else{
                System.out.println("El numero ingresado "+numero+" es IMPAR.");
            }
            
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
        System.out.println("El numero ingresado es "+numero+". Finaliza el programa.");
    }
}
