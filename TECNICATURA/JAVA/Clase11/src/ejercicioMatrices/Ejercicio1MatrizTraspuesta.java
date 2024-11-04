/* Ejercicio 1:
Crear y cargar una matriz de tamaño 3x3, trasponerla y mostrarla
 */
package ejercicioMatrices;

public class Ejercicio1MatrizTraspuesta {
    
    public static void main(String[] args) {
        
        int matriz[][] = new int[3][3]; // creamos la matriz
        
        matriz[0][0] = 10; //Llenamos la matriz
        matriz[0][1] = 20;
        matriz[0][2] = 30;
        matriz[1][0] = 40;
        matriz[1][1] = 50;
        matriz[1][2] = 60;
        matriz[2][0] = 70;
        matriz[2][1] = 80;
        matriz[2][2] = 90;
        
        // Mostramos la matriz original
        System.out.println("Matriz original:");
        imprimir(matriz); // Llama al método para imprimir la matriz
        
        int matrizTranspuesta[][] = new int[3][3]; // Matriz traspuesta de 3x3
        
        for (int fila = 0; fila < matriz.length; fila++) { // Recorremos filas
            for (int columna = 0; columna < matriz[fila].length; columna++) { // Recorremos columnas
                matrizTranspuesta[columna][fila] = matriz[fila][columna]; // Asignamos el valor transpuesto, es decir cambiamos filas por columnas
            }
        }
        
        // Mostramos la matriz traspuesta
        System.out.println("\nMatriz traspuesta:");
        imprimir(matrizTranspuesta); // Llamamos al método para imprimir la matriz traspuesta
    }
      
         public static void imprimir(int matriz[][]){
         for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("[" + matriz[i][j] + "] ");
            }
            System.out.println(); 
        }
    }
}