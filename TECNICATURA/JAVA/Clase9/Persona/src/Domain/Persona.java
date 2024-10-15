package Domain;

public class Persona {
    // Atributos de herencia
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;

    // Constructor vacío: este es para crear objetos sin necesidad de inicializar
    // los atributos de la clase
    public Persona() {
        // Constructor body goes here (if needed)
    }

    // Constructor con solo nombre
    public Persona(String nombre) { // Constructor 2
        this.nombre = nombre;
    }

    // Constructor completo
    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;


    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }


    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", genero=" + genero +
                ", edad=" + edad +
                ", direccion='" + direccion + '\'' +
                '}';
    }
}
