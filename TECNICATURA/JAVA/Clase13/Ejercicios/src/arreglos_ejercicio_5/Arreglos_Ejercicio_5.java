/*
 Ejercicio 5: leer 10 números enteros en una tabla. Guardar en otra tabla los
elementos pares de la primera, y a continuación los elementos impares.
 */
package arreglos_ejercicio_5;

import java.util.Scanner;

public class Arreglos_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        int conteo_pares=0, conteo_impares=0;
        
        System.out.println("Llenar arreglo: ");
        for(int i=0; i<10; i++){
            System.out.print((i+1)+". Ingrese un número: ");
            arreglo[i] = entrada.nextInt();
            
            if(arreglo[i]%2==0){ //contamos para crear los arreglos
                conteo_pares++;
            }
            else{
                conteo_impares++;
            }
        }
        
        //Creamos los arreglos pares e impares
        int par[] = new int[conteo_pares];
        int impar[] = new int[conteo_impares];
        
        conteo_pares=0; //usamos como iteradores
        conteo_impares=0;
        
        for(int i=0; i<10; i++){
            if(arreglo[i]%2==0){
                par[conteo_pares] = arreglo[i];
                conteo_pares++;
            }
            else{
                    impar[conteo_impares] = arreglo[i];
                    conteo_impares++;
            }
        }
        System.out.print("\nArreglo ingresado: ");
        for(int i=0; i<10; i++){
            System.out.print(arreglo[i]+" - ");
        }
        
        System.out.print("\nArreglo pares: ");
        for(int i=0; i<conteo_pares; i++){
            System.out.print(par[i]+" - ");
        }
        
        System.out.print("\nArreglo impares: ");
        for(int i=0; i<conteo_impares; i++){
            System.out.print(impar[i]+" - ");
        }
        System.out.println();
    }
}
