
package domain;

public class Persona {
    public String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona {");
        sb.append("nombre = ").append(this.nombre);
        sb.append(", direccion en memoria = ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
}
