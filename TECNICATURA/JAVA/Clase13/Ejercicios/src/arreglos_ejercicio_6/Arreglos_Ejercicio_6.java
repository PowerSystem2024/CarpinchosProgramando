/*
 Ejercicio 6: leer dos series de 10 enteros, que estarán ordenados crecientemente.
Copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenados.
 */
package arreglos_ejercicio_6;

import java.util.Scanner;

public class Arreglos_Ejercicio_6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        int a[] = new int[10];
        int b[] = new int[10];
        int c[] = new int[20];
        boolean creciente = true;
        
        System.out.println("Llenar el primer arreglo: ");
        do{
            for(int i=0; i<10; i++){
                System.out.println((i+1)+". Ingrese un número: ");
                a[i] = entrada.nextInt();
            }
            //Comprobamos si el arreglo esta ordenado
            for(int i=0; i<9; i++){
                if(a[i] < a[i+1]){ //creciente 1-2-3
                    creciente = true;
                }
                if(a[i] > a[i+1]){ //decreciente 3-2-1
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false){
                System.out.println("\nEl arreglo esta desordenado, vuelva a ingresar: ");
            }
        }while(creciente == false);
        
        System.out.println("Llenar el segundo arreglo: ");
        do{
            for(int i=0; i<10; i++){
                System.out.println((i+1)+". Ingrese un número: ");
                b[i] = entrada.nextInt();
            }
            for(int i=0; i<9; i++){
                if(b[i] < b[i+1]){
                    creciente = true;
                }
                if(b[i] > b[i+1]){
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false){
                System.out.println("\nEl arreglo esta desordenado, vuelva a ingresar: ");
            }
        }while(creciente == false);
        
        int i=0; //iterador i para arreglo a
        int j=0; //iterador j para arreglo b
        int k=0; //iterador k para arreglo c
        
        while(i<10 && j<10){
            if(a[i] < b[j]){ //si el elemento de a es menor de b
                    c[k] = a[i]; //copiamos el elemento de a
                    i++; //avanzamos una posicion en a
            }
            else{
                    c[k] = b[j]; //copiamos el elemento de b
                    j++; //avanzamos una posición mas en b
            }
            k++; //avanzamos una posicion mas en c
        }
        
        //cuando salimos del while es porque un arreglo(a o b),se ha copiado completo
        if(i==0){ //significa queya copiamos todo el arreglo a, falta el b
            while(j<10){ //mientras el iterador sea menor a 10
                c[k] = b[j]; //copiamos el elemento de b en c
                j++; //avanzamos una posicion en b
                k++; //avanzamos una posicion en c                
            }
        }
        else{ //significa que ya copiamos todo el arreglo b, falta el a
                while(i<10){
                    c[k] = a[i];
                    i++;
                    k++;
                }
        }
        
        System.out.println("\nEl arreglo c completo es: ");
        for(k=0; k<20; k++){
            System.out.println(c[k]+" - ");
        }
        System.out.println();
    }
}
