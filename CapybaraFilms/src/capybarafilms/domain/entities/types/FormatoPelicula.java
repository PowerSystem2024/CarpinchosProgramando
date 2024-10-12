package capybarafilms.domain.entities.types;

// Esta clase define un enum para los formatos de las películas
public enum FormatoPelicula {

    // Definimos dos formatos: 2D y 3D, con sus respectivos precios extra
    DOS_D("2D", 0), // Formato 2D sin costo adicional
    TRES_D("3D", 1000); // Formato 3D con un costo adicional de 1000

    private String tipo; // Variable que almacena el tipo de formato
    private double precioExtra; // Variable que almacena el precio extra del formato

    // Constructor que inicializa el tipo y el precio extra del formato
    private FormatoPelicula(String tipo, double precioExtra) {
        this.tipo = tipo; // Asigna el tipo de formato
        this.precioExtra = precioExtra; // Asigna el precio extra
    }

    // Método que devuelve el tipo de formato
    public String getTipo() {
        return tipo; // Retorna el tipo de formato (2D o 3D)
    }

    // Método que devuelve el precio extra del formato
    public double getPrecioExtra() {
        return precioExtra; // Retorna el precio extra correspondiente
    }
}