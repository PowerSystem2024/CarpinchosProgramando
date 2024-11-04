/*
Ejercicio: Clases - Proyecto Caja
    Crear un proyecto según las especificaciones mostradas a continuación.
    Fórmula:
        volumen = ancho * alto * profundidad
*/

// Constructor que reciba los argumentos.
// Crear dos objetos: uno vacío y otro con argumentos.

package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        // Estableciendo valores de la caja.
        int anchoCaja = 3;
        int altoCaja = 5;
        int profundidadCaja = 8;
        
        System.out.println("El ancho de la caja es: " + anchoCaja);
        System.out.println("El alto de la caja es: " + altoCaja);
        System.out.println("La profundidad de la caja es: " + profundidadCaja);
        
        // Creación de objeto1 - vacío
        Caja caja1 = new Caja();
        // Pasaje de valores
        caja1.ancho = anchoCaja;
        caja1.alto = altoCaja;
        caja1.profundidad = profundidadCaja;
        
        int resultadoFormula = caja1.formulaCaja();
        
        System.out.println("");
        System.out.println("El volumen de la caja 1 es: " + resultadoFormula);
        
        // Creación de objeto2 - con argumentos
        Caja caja2 = new Caja(4, 8, 9);
        System.out.println("El volumen de la caja 2 es: " + caja2.formulaCaja());
    }
    
}
