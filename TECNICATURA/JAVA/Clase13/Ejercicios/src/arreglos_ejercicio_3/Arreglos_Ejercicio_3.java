/*
 Ejericio 3: Leer 5 elementos numéricos que se introducirán ordenados de forma
creciente.Éstos los guardaremos en una tabla de tamaño 10. Leer un número N, e
insertarlo en el lugar adecuado para que la tabla continúe ordenada.
 */
package arreglos_ejercicio_3;

import java.util.Scanner;


public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        boolean creciente = true;
        int numero, sitio_num=0, j=0;
        
        System.out.println("Llenar el arreglo: ");
        do{
            //llenado del arreglo
            for(int i=0; i<5; i++){
                System.out.println((i+1)+". Ingrese un número: ");
                arreglo[i] = entrada.nextInt();
            }
            //comprobar si el arreglo esta ordenado en orden creciente
            for(int i=0; i<4; i++){
                if(arreglo[i] < arreglo[i+1]){
                creciente = true;
                }
                if(arreglo[i] > arreglo[i+1]){
                    creciente = false;
                    break;
                }
            }
            if(creciente == false){
                System.out.println("\nEl arreglo no está ordenado en forma creciente, vuelva a ingresar\n");
            }
        }while(creciente == false);
        
        System.out.println("Ingrese un número a insertar: ");
        numero = entrada.nextInt();
        
        //Esto es para darnos cuenta en que posición va en número
        while(arreglo[j]<numero && j<5){
            sitio_num++;
            j++;
        }
        //trasladamos una posición en el arreglo a los elementos que van detras de número
        for(int i=4; i>=sitio_num; i--){
            arreglo[i+1] = arreglo[i];
        }
        //insertamos el número
        arreglo[sitio_num] = numero;
        
        System.out.println("\nEl arreglo queda: ");
        for(int i=0; i<6; i++){
            System.out.println(arreglo[i]+" - ");
        }
        System.out.println();
    }
}
