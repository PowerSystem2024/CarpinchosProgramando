
package clase6;

public class SobrecargaDeMetodos {
    int a;
    int b;
    // CONSTRUCTORES Y SOBRECARGA DE CONSTRUCTORES
    /* Constructor -> Método especial.
            - Construye un objeto.
            - Reserva un espacio de memoria.
            - Inicializa los atributos de la clase.
    */
    // Constructor por defecto
    // Constructor 1 - Sin parámetros (Omitiendo valores, vacío)
    public SobrecargaDeMetodos(){ 
        System.out.println("Se está ejecutando este constructor número uno.");
    }
    
    // Sobrecarga de Constructores
    // Constructor 2 - Con parámetros (Asignando valores, inicializando atributos)
    public SobrecargaDeMetodos(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando este constructor número dos.");
    }
    
}
