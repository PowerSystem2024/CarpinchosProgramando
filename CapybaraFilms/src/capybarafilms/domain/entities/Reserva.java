package capybarafilms.domain.entities;

import capybarafilms.domain.entities.types.Ubicacion;
import java.util.List;

public class Reserva {

    private final Sala sala; // La sala donde se realizará la proyección.
    private final Candy candy; // El combo que se ha comprado (puede ser null si no se compra).
    private final Cliente cliente; // El cliente que realiza la reserva.
    private final List<Butaca> butacasAsignadas; // Lista de butacas que se han reservado para el cliente.

    // Constructor que inicializa la reserva con el cliente, sala, combo y butacas.
    public Reserva(Cliente cliente, Sala sala, Candy candy, List<Butaca> butacasAsignadas) {
        this.sala = sala; // Asigna la sala a la reserva.
        this.candy = candy; // Asigna el combo (si existe) a la reserva.
        this.cliente = cliente; // Asigna el cliente a la reserva.
        this.butacasAsignadas = butacasAsignadas; // Asigna las butacas reservadas.
    }

    // Método para obtener la sala de la reserva.
    public Sala getSala() {
        return sala;
    }

    // Método para obtener el combo de la reserva (puede ser null).
    public Candy getCandy() {
        return candy;
    }

    // Método para obtener el cliente de la reserva.
    public Cliente getCliente() {
        return cliente;
    }

    // Método que calcula el precio total de la reserva.
    public double getPrecioTotal() {
        double total = 0; // Inicializa el total en cero.
        for (Butaca butaca : butacasAsignadas) {
            Ubicacion ubicacion = butaca.getUbicacion(); // Obtiene la ubicación de la butaca.
            if (ubicacion != null) {
                total += sala.precioDeEntrada(ubicacion); // Suma el precio de la entrada al total.
            } else {
                System.out.println("Error: La ubicación de la butaca es nula."); // Mensaje de error si la ubicación es nula.
            }
        }
        if (candy != null) {
            total += candy.getTipo().getPrecio(); // Suma el precio del combo si existe.
        }
        return total; // Devuelve el total calculado.
    }

    // Método que muestra un resumen de la reserva.
    public void mostrarResumen() {
        System.out.println("Resumen de la Reserva:");
        System.out.println("Cliente: " + cliente.getNombre() + " " + cliente.getApellido()); // Muestra el nombre del cliente.
        System.out.println("Sala: " + sala.toString()); // Muestra la sala.
        System.out.println("Butacas Reservadas:");

        double totalEntradas = 0; // Inicializa el total de entradas en cero.
        for (Butaca butaca : butacasAsignadas) {
            String tipo = butaca.getCategoria().getNombre(); // Obtiene el tipo de butaca.
            double precioEntrada = sala.precioDeEntrada(butaca.getUbicacion()); // Obtiene el precio de la entrada.
            totalEntradas += precioEntrada; // Suma al total de entradas.
            System.out.println(" - Fila: " + butaca.getUbicacion().getFila()
                    + ", Butaca: " + butaca.getUbicacion().getButaca()
                    + " | Tipo: " + tipo
                    + " | Precio: " + precioEntrada); // Muestra la información de la butaca.
        }

        if (candy != null) {
            double precioCombo = candy.getTipo().getPrecio(); // Obtiene el precio del combo.
            System.out.println("Combo elegido: " + candy.getTipo().getNombre()
                    + " | Precio: " + precioCombo); // Muestra información del combo.
        } else {
            System.out.println("No se eligió combo."); // Indica que no se eligió combo.
        }

        double total = totalEntradas + (candy != null ? candy.getTipo().getPrecio() : 0); // Calcula el total final.
        System.out.println("Total a Pagar: " + total); // Muestra el total a pagar.
    }
}