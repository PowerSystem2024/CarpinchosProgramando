package domain;

public class Persona {

    public final static int CONSTANTE_AQUI = 15;// El formato en mayúscula(se agrega con guión bajo) nos dice que es una Cte
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void imprimir() {
        System.out.println("Método para imprimir");
    }
}
