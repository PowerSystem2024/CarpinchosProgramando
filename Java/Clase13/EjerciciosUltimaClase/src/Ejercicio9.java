public class Ejercicio9 {
/*

*/
    public static void main(String[] args) {
        int[][] matriz = new int[5][5];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                if (i == 0 || i == 4 || j == 0 || j == 4) {
                    matriz[i][j] = 1; 
                } else {
                    matriz[i][j] = 0; 
                }
            }
        }
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
