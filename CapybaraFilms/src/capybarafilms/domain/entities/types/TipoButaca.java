package capybarafilms.domain.entities.types;

// Esta clase define un enum para los tipos de butacas disponibles
public enum TipoButaca {

    // Definimos dos tipos de butacas: Común y Premium, con sus respectivos precios
    COMUN("comun", 2000), // Butaca común con un precio de 2000
    PREMIUM("premium", 3500); // Butaca premium con un precio de 3500

    private final String nombre; // Variable que almacena el nombre del tipo de butaca
    private final double precio; // Variable que almacena el precio del tipo de butaca

    // Constructor que inicializa el nombre y el precio del tipo de butaca
    private TipoButaca(String nombre, double precio) {
        this.nombre = nombre; // Asigna el nombre del tipo de butaca
        this.precio = precio; // Asigna el precio del tipo de butaca
    }

    // Método que devuelve el nombre del tipo de butaca
    public String getNombre() {
        return nombre; // Retorna el nombre del tipo de butaca
    }

    // Método que devuelve el precio del tipo de butaca
    public double getPrecio() {
        return precio; // Retorna el precio correspondiente
    }
}
