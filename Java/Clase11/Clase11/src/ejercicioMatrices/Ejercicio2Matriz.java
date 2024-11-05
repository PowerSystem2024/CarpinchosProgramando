/*
Ejercicio 2:
Crear una matriz de tama�o 7x7 y rellenarla de forma que los elementos de la
diagonal principal sean 1 y el resto 0
 */
package ejercicioMatrices;

public class Ejercicio2Matriz {

    public static void main(String[] args) {

        int matriz[][] = new int[7][7]; // Inicializamos la matriz

        for (int fila = 0; fila < 7; fila++) { //En este ciclo for recorremos filas
            for (int columna = 0; columna < 7; columna++) { //recorremos columnas
                if (fila == columna) { // En este if validamos si fila y columna tienen el mismo numero pertenecen a la diagonal principal
                    matriz[fila][columna] = 1; // Si pertenecen les asignamos 1
                } else {
                    matriz[fila][columna] = 0; //sino, les asignamos 0
                }
            }
        }
        System.out.println("Matriz de 7x7 ");
        imprimir(matriz); // invocamos al metodo imprimir

    }

    public static void imprimir(int matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("[" + matriz[i][j] + "] ");
            }
            System.out.println();
        }
    }
}
