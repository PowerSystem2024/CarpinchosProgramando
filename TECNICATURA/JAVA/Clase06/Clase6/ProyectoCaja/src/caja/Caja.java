// Ejercicio: Clases - Proyecto Caja

// Constructor Vacío.
// Método para sacar el volumen de la caja.

package caja;

public class Caja {
    // Atributos
    int ancho;
    int alto;
    int profundidad;
    
    // Métodos y Constructores
    // Constructor 1 - Vacío
    public Caja(){
        
    }
    
    // Constructor 2 - Con Parámetros
    public Caja(int ancho, int alto, int profundidad){
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    // Método para calcular el volumen
    public int formulaCaja(){
        return ancho * alto * profundidad;
    }
}  
