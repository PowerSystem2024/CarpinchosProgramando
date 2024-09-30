package capybarafilms;

public class Candy {
     private String tipo;  // Sería chico, mediano o grande.
    private double precio;

    public Candy(String tipo, double precio) {
        this.tipo = tipo;
        this.precio = precio;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Candy: Tamaño: " + tipo + ", precio: " + precio;
    }
}