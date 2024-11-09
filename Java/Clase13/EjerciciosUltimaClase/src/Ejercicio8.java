import java.util.Random;

public class Ejercicio8 {

    public static void main(String[] args) {
        int filas = 5;
        int columnas = 9;

        int[][] matrizOriginal = new int[filas][columnas];
        int[][] matrizTranspuesta = new int[columnas][filas];

        Random random = new Random();
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matrizOriginal[i][j] = random.nextInt(10); 
            }
        }
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matrizTranspuesta[j][i] = matrizOriginal[i][j];
            }
        }
        System.out.println("Matriz Original (5x9):");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                System.out.print(matrizOriginal[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("\nMatriz Transpuesta (9x5):");
        for (int i = 0; i < columnas; i++) {
            for (int j = 0; j < filas; j++) {
                System.out.print(matrizTranspuesta[i][j] + " ");
            }
            System.out.println();
        }
    }
}

