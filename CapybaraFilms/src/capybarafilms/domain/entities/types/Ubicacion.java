package capybarafilms.domain.entities.types;

// Esta clase representa la posición de una butaca en el cine.
public class Ubicacion {
    
    private int fila; // Aquí guardamos el número de fila de la butaca.
    private int butaca; // Aquí guardamos el número de la butaca en esa fila.

    // Constructor que inicializa la fila y la butaca.
    public Ubicacion(int fila, int butaca) {
        super();
        this.fila = fila;      // Asignamos el número de fila.
        this.butaca = butaca;  // Asignamos el número de la butaca.
    }
    
    // Este método devuelve el número de fila.
    public int getFila() { 
        return fila;
    }
    
    // Este método permite cambiar el número de fila.
    public void setFila(int fila) { 
        this.fila = fila; // Actualiza el número de fila.
    }
   
    // Este método devuelve el número de la butaca.
    public int getButaca() {  
        return butaca;
    }

    // Este método permite cambiar el número de la butaca.
    public void setButaca(int butaca) { 
        this.butaca = butaca; // Actualiza el número de la butaca.
    }
}