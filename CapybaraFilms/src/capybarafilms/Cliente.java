package capybarafilms;

public class Cliente {

    //caracteristicas del cliente

    String nombre;
    String apellido;
    String dni;
    String eMail;

    public Cliente(String nombre, String apellido, String dni, String eMail) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.dni = dni;
        this.eMail = eMail;




    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String geteMail() {
        return eMail;
    }

    public void seteMail(String eMail) {
        this.eMail = eMail;


    }

    @Override
    public String toString() {
        return "Cliente: \n" +
                "  Nombre: " + nombre + "\n" +
                "  Apellido: " + apellido + "\n" +
                "  DNI: " + dni + "\n" +
                "  eMail: " + eMail;
    }




}
