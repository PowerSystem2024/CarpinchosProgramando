package capybarafilms.test;

import java.util.List;

import capybarafilms.domain.entities.Butaca;
import capybarafilms.domain.entities.Candy;
import capybarafilms.domain.entities.Catalogo;
import capybarafilms.domain.entities.Cliente;
import capybarafilms.domain.entities.Pelicula;
import capybarafilms.domain.entities.Reserva;
import capybarafilms.domain.entities.Sala;
import capybarafilms.domain.services.ServicioCompraEntradas;
import capybarafilms.domain.services.ServicioValidacion;

public class ComprarEntradaTest {
    public static void main(String[] args) {
        ServicioValidacion validacion = new ServicioValidacion(); // Instanciamos un servicio de validación
        ServicioCompraEntradas servicioCompra = new ServicioCompraEntradas(); // Instanciamos un servicio de compra

        servicioCompra.iniciarCompra(); // Invoca el método para mostrar el mensaje de bienvenida
        
        // Obtener datos del cliente
        Cliente cliente = validacion.obtenerDatosCliente();

        // Mostrar y seleccionar película
        servicioCompra.mostrarPeliculas();
        int peliculaIndex = servicioCompra.seleccionarPelicula();

        // Seleccionar cantidad de entradas
        int cantidadEntradas = servicioCompra.solicitarCantidadEntradas();

        // Seleccionar combo de Candy
        Candy candy = null; // Implementar lógica si es necesario

        // Obtener la película y crear la sala
        Pelicula peliculaSeleccionada = Catalogo.getPeliculas().get(peliculaIndex);
        Sala sala = new Sala(peliculaSeleccionada);

        // Seleccionar butacas
        List<Butaca> butacasAsignadas = servicioCompra.seleccionarButacas(cantidadEntradas, sala);

        // Realizar la reserva
        Reserva reserva = servicioCompra.realizarReserva(cliente, sala, candy, butacasAsignadas);

        // Mostrar el resumen de la reserva
        reserva.mostrarResumen();

        System.out.println("¡Gracias por su compra, " + cliente.getNombre() + "!");
    }
}