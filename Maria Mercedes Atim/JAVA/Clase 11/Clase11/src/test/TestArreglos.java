package test;

public class TestArreglos {
    
    public static void main(String[] args) {
        
        int edades[] = new int [3]; // Primero se declara la variable. Despues del = se instancia un objeto del tipo arreglo.
        System.out.println("edades = " + edades); // nos muestra la posicion en memoria
        
        edades[0] = 17; //Guardamos la primera edad en el indice 0 del array (posicion 1)
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 20; //Guardamos otra edad en el indice 1 del array (posicion 2)
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 35; //Guardamos otra edad en el indice 2 del array (posicion 3)
        System.out.println("edades 2 = " + edades[2]);
        
        //edades[3] = 7; //Queda fuera de rango porque dimensionamos el arreglo con 3 posiciones
        
        for (int i = 0; i < edades.length; i++){ // Recorre cada posicion del arreglo
            System.out.println("En el arreglo edades, en la posicion " + i + " está la edad: "+ edades[i]);
        }
    }    
}