/* Contexto Estático */
package domain;

public class Persona {

    private int idPersona;
    private static int contadorPersona;
    private String nombre;

    public Persona(String nombre) {
        this.idPersona = idPersona;
        this.nombre = nombre;
        // Incrementar el contador por cada objeto nuevo.
        Persona.contadorPersona++; //No usar el operador this
        // Vamos a asignar un nuevo valor alavariableidPersona
        this.idPersona = Persona.contadorPersona;
    }

    public int getIdPersona() {
        return idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int contadorPersona) {
        Persona.contadorPersona = contadorPersona;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona: " + "idPersona: " + idPersona + ", nombre: " + nombre ;
    }   
}