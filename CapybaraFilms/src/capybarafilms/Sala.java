
// Clase Sala

import capybarafilms.Butaca;

public class Sala {
    private Butaca[] butacas; // Array de butacas
    private int capacidad;

    // Constructor
    public Sala(Butaca[] butacas, int capacidad) {
        this.butacas = butacas;
        this.capacidad = capacidad;
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

    // Método toString
    @Override
    public String toString() {
        StringBuilder butacasInfo = new StringBuilder();
        for (Butaca butaca : butacas) {
            butacasInfo.append(butaca.toString()).append("\n");
        }

        return "Sala{" +
                "capacidad=" + capacidad +
                ", butacas=\n" + butacasInfo.toString() +
                '}';
    }
}
