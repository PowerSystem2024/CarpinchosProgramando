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
        ServicioValidacion validacion = new ServicioValidacion(); 
        ServicioCompraEntradas servicioCompra = new ServicioCompraEntradas(); 

        servicioCompra.iniciarCompra(); 

        Cliente cliente = validacion.obtenerDatosCliente();
        System.out.println("");
    
        servicioCompra.mostrarPeliculas();
        int peliculaIndex = servicioCompra.seleccionarPelicula();
        System.out.println("");
        
        int cantidadEntradas = servicioCompra.solicitarCantidadEntradas();
        System.out.println("");
        
        Pelicula peliculaSeleccionada = Catalogo.getPeliculas().get(peliculaIndex);
        Sala sala = new Sala(peliculaSeleccionada);
        System.out.println("");

        List<Butaca> butacasAsignadas = servicioCompra.seleccionarButacas(cantidadEntradas, sala);
        System.out.println("");
        
        Candy combo = servicioCompra.seleccionarCombo();
        System.out.println("");
        
        Reserva reserva = servicioCompra.realizarReserva(cliente, sala, combo, butacasAsignadas);
        System.out.println("");
        
        reserva.mostrarResumen();
        System.out.println("");    

        System.out.println("¡Gracias por su compra, " + cliente.getNombre() + "! Disfrute la funcion!");
    }
}