package capybarafilms.domain.entities.types;

// Esta clase define un enum para los tipos de combos disponibles
public enum TipoCandy { // Un enum se usa para definir un conjunto fijo de constantes

    // Definimos valores válidos para los tamaños de los combos:
    CHICO("chico", 2500), // Combo chico con un precio de 2500
    MEDIANO("mediano", 3500), // Combo mediano con un precio de 3500
    GRANDE("grande", 5000); // Combo grande con un precio de 5000

    private String nombre; // Nombre del tamaño del combo
    private double precio; // Precio del combo

    // Constructor que inicializa el nombre y el precio del combo
    private TipoCandy(String nombre, double precio) { 
        this.nombre = nombre; // Asigna el nombre del tamaño del combo
        this.precio = precio; // Asigna el precio del combo
    }   

    // Método que devuelve el nombre del tamaño del combo
    public String getNombre() { 
        return nombre; // Retorna el nombre del tamaño del combo
    }

    // Método que devuelve el precio del combo
    public double getPrecio() {  
        return precio; // Retorna el precio correspondiente
    }      
}