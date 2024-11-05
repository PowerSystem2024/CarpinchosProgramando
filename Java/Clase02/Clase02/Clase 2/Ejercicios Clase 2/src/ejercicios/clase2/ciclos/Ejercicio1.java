// Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo.
package ejercicios.clase2.ciclos;
import java.util.Scanner;
public class Ejercicio1 {
    
    public static void main(String[] args) {
        
        //-----------   con Scanner ----------------
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese un número para calcular su cuadrado: ");
        int numero = entrada.nextInt();
        
       while( numero > 0){
            System.out.println("El cuadrado de " + numero + " es: " + numero*numero);
            System.out.println("Ingrese otro número para calcular su cuadrado: ");
            numero = entrada.nextInt();
       }
        System.out.println("Ha ingresado cero o un numero negativo, finalizó el programa.");
    }    
}