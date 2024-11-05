package test;

import domain.Persona;

public class TestMatrices {

    public static void main(String[] args) {
        int edades[][] = new int[3][2]; //creamos una matriz tipo int
        System.out.println("edades = " + edades); // nos muestra el espacio en memoria

        edades[0][0] = 5; // Llenamos cada posicion de la matriz
        edades[0][1] = 7;
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 2;
        edades[2][1] = 9;

        System.out.println("En la matriz edades, en la fila: 0, columna 0 est� el numero: " + edades[0][0]);
        System.out.println("En la matriz edades, en la fila: 0, columna 1 est� el numero: " + edades[0][1]);
        System.out.println("En la matriz edades, en la fila: 1, columna 0 est� el numero: " + edades[1][0]);
        System.out.println("En la matriz edades, en la fila: 1, columna 1 est� el numero: " + edades[1][1]);
        System.out.println("En la matriz edades, en la fila: 2, columna 0 est� el numero: " + edades[2][0]);
        System.out.println("En la matriz edades, en la fila: 2, columna 1 est� el numero: " + edades[2][1]);

        // Imprimimos la matriz en un formato visual
        System.out.println("\nMatriz de edades: ");
        for (int fila = 0; fila < edades.length; fila++) { // Recorremos las filas de la matriz
            for (int columna = 0; columna < edades[fila].length; columna++) { // Recorremos las columnas de la fila actual
                //System.out.println("edades "+fila+"-"+columna+": "+edades[fila][columna]);
                System.out.print("[" + edades[fila][columna] + "] "); // Imprimimos el n�mero con corchetes
            }
            System.out.println(); // Saltamos a la siguiente l�nea despu�s de imprimir una fila
        }

        //Sintaxis clasica
        //String frutas[][] = new String[3][2]; // Definimos la variable y despues instanciamos la matriz de tipo String.
        //Sintaxis simplificada
        System.out.println("\nMatriz de Verduras: ");
        String frutas[][] = {{"Lechuga", "Tomate"}, {"Cebolla", "Zanahoria"}, {"Papa", "Acelga"}};
        imprimir(frutas);
//        for (int i = 0; i < frutas.length; i++) {
//            for (int j = 0; j < frutas[i].length; j++) {
//                System.out.print("[" + frutas[i][j] + "] ");
//            }
//            System.out.println();
//        }

        //Creamos matriz de objetos
        System.out.println("\nMatriz de objetos Persona ");
        Persona personas[][] = new Persona[2][3]; // Definimos la variable y despues instanciamos la matriz de tipo Persona.
        personas[0][0] = new Persona("Wanda");
        personas[0][1] = new Persona("Ana Paula");
        personas[0][2] = new Persona("Nelson");
        personas[1][0] = new Persona("Mariana");
        personas[1][1] = new Persona("Nicolas");
        personas[1][2] = new Persona("Melina");
        imprimir2(personas);
    }

    public static void imprimir(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("[" + matriz[i][j] + "] ");
            }
            System.out.println();
        }
    }

    public static void imprimir2(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("edades "+i+"-"+j+": "+matriz[i][j]);
            }
            System.out.println();
        }
    }
}