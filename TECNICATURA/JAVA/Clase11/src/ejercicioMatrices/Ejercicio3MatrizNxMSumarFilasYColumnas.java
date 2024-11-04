/*
 Ejercicio 3:
Crear y cargar una matriz de tamaño nxm, mostrar la suma de cada fila y columna.
 */
package ejercicioMatrices;

import java.util.Scanner;

public class Ejercicio3MatrizNxMSumarFilasYColumnas {

    public static void main(String[] args) {
        int fila = 0, columna = 0; // inicializamos fila y columna
        int sumaFila = 0, sumaColumna = 0; // inicializamos las variables que guardaran el resultado de las filas y columnas

        Scanner entrada = new Scanner(System.in);

        System.out.println("Por favor ingrese la dimension de fila: "); // solicitamos al usuario que ingrese la cantidad de filas
        fila = entrada.nextInt();

        System.out.println("Por favor ingrese la dimension de columna: "); // solicitamos la cantidad de columnas
        columna = entrada.nextInt();

        int matriz[][] = new int[fila][columna]; // Le asignamos a la matriz las dimensiones ingresadas por el usuario
        
        llenarMatriz(matriz, fila, columna); // Invocamos al metodo llenar matriz
        imprimir(matriz); // Invocamos al metodo imprimir matriz para mostrarla

        System.out.println("");
        
        for (int i = 0; i < fila; i++) { // En este ciclo for recorremos las filas
            for (int j = 0; j < columna; j++) {
                sumaFila += matriz[i][j]; // en la variable SumaFila guardamos el resultado de la suma de cada fila
            }
            System.out.println("La fila " + i + " suma: " + sumaFila); // Mostramos el resultado
            sumaFila = 0; // limpiamos el resultado para que cuando itere nuevamente no nos sume la fila anterior
        }
        
        System.out.println(""); // colocamos un salto de linea para mejor legibilidad
        
        for (int i = 0; i < columna; i++) { // En este For recorremos las columnas
            for (int j = 0; j < fila; j++) {
                sumaColumna += matriz[j][i]; // guardamos en la variable sumaColumna la suma de las columnas
            }
            System.out.println("La columna " + i + " suma: " + sumaColumna); // mostramos el resultado
            sumaColumna = 0; // limpiamos el resultado
        }
    }

    public static void llenarMatriz(int matriz[][], int pFila, int pColumna) { // este metodo llena la matriz 
        for (int fila = 0; fila < pFila; fila++) {
            for (int columna = 0; columna < pColumna; columna++) {
                matriz[fila][columna] = (int) (Math.random() * 10); // Con numeros aleatorios de 0 a 9
            }
        }
    }

    public static void imprimir(int matriz[][]) { // este metodo muestra la matriz
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("[" + matriz[i][j] + "] ");
            }
            System.out.println();
        }
    }
}
