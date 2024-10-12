package capybarafilms.domain.entities;

public class Cliente {

    // Características del cliente
    String nombre; // Almacena el nombre del cliente
    String apellido; // Almacena el apellido del cliente
    String dni; // Almacena el DNI del cliente
    String eMail; // Almacena el email del cliente

    // Constructor que inicializa los atributos del cliente
    public Cliente(String nombre, String apellido, String dni, String eMail) {
        this.nombre = nombre; // Asigna el nombre
        this.apellido = apellido; // Asigna el apellido
        this.dni = dni; // Asigna el DNI
        this.eMail = eMail; // Asigna el email
    }

    // Método para obtener el nombre del cliente
    public String getNombre() {
        return nombre;
    }

    // Método para establecer un nuevo nombre al cliente
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // Método para obtener el apellido del cliente
    public String getApellido() {
        return apellido;
    }

    // Método para establecer un nuevo apellido al cliente
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    // Método para obtener el DNI del cliente
    public String getDni() {
        return dni;
    }

    // Método para establecer un nuevo DNI al cliente
    public void setDni(String dni) {
        this.dni = dni;
    }

    // Método para obtener el email del cliente
    public String geteMail() {
        return eMail;
    }

    // Método para establecer un nuevo email al cliente
    public void seteMail(String eMail) {
        this.eMail = eMail;
    }

    // Método que devuelve una representación en texto del cliente
    @Override
    public String toString() {
        return "Cliente: \n"
                + "  Nombre: " + nombre + "\n"
                + "  Apellido: " + apellido + "\n"
                + "  DNI: " + dni + "\n"
                + "  eMail: " + eMail; // Muestra toda la información del cliente
    }
}