package capybarafilms;

import capybarafilms.Butaca;

public class Sala {
    private Butaca[] butacas; // Array de butacas
    private int capacidad;
    private String categoria;

    // Constructor

    public Sala(Butaca[] butacas, int capacidad, String categoria) {
        this.butacas = butacas;
        this.capacidad = capacidad;
        this.categoria = categoria;
    }
   
    // Getters y Setters

    public Butaca[] getButacas() {
        return butacas;
    }

    public void setButacas(Butaca[] butacas) {
        this.butacas = butacas;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public void setCapacidad(int capacidad) {
        this.capacidad = capacidad;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    // Método toString
    @Override
    public String toString() {
        return "Sala{" + "butacas=" + butacas + ", capacidad=" + capacidad + ", categoria=" + categoria + '}';
    }
}