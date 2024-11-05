package capybarafilms.test; // Define el paquete de la clase de prueba

import java.util.List; // Importa la clase List para manejar listas

// Importa las entidades necesarias desde el paquete domain.entities
import capybarafilms.domain.entities.Butaca;
import capybarafilms.domain.entities.Candy;
import capybarafilms.domain.entities.Catalogo;
import capybarafilms.domain.entities.Cliente;
import capybarafilms.domain.entities.Pelicula;
import capybarafilms.domain.entities.Reserva;
import capybarafilms.domain.entities.Sala;
import capybarafilms.domain.services.ServicioCompraEntradas; // Importa el servicio de compra de entradas
import capybarafilms.domain.services.ServicioValidacion; // Importa el servicio de validación de datos

public class ComprarEntradaTest { // Clase principal para probar la compra de entradas

    public static void main(String[] args) { // Método main que se ejecuta al iniciar el programa
        ServicioValidacion validacion = new ServicioValidacion(); // Crea una instancia del servicio de validación
        ServicioCompraEntradas servicioCompra = new ServicioCompraEntradas(); // Crea una instancia del servicio de compra de entradas

        servicioCompra.iniciarCompra(); // Inicia el proceso de compra
        System.out.println(""); // Imprime una línea en blanco

        Cliente cliente = validacion.obtenerDatosCliente(); // Obtiene los datos del cliente mediante validación
        System.out.println(""); // Imprime una línea en blanco

        servicioCompra.mostrarPeliculas(); // Muestra la lista de películas disponibles
        int peliculaIndex = servicioCompra.seleccionarPelicula(); // Permite al usuario seleccionar una película
        System.out.println(""); // Imprime una línea en blanco

        int cantidadEntradas = servicioCompra.solicitarCantidadEntradas(); // Solicita la cantidad de entradas que desea comprar
        System.out.println(""); // Imprime una línea en blanco

        Pelicula peliculaSeleccionada = Catalogo.getPeliculas().get(peliculaIndex); // Obtiene la película seleccionada del catálogo
        Sala sala = new Sala(peliculaSeleccionada); // Crea una nueva sala basada en la película seleccionada
        System.out.println(""); // Imprime una línea en blanco

        List<Butaca> butacasAsignadas = servicioCompra.seleccionarButacas(cantidadEntradas, sala); // Selecciona las butacas según la cantidad solicitada y la sala
        System.out.println(""); // Imprime una línea en blanco

        Candy combo = servicioCompra.seleccionarCombo(); // Permite al usuario seleccionar un combo de snacks
        System.out.println(""); // Imprime una línea en blanco

        Reserva reserva = servicioCompra.realizarReserva(cliente, sala, combo, butacasAsignadas); // Realiza la reserva de entradas y combo para el cliente
        System.out.println(""); // Imprime una línea en blanco

        reserva.mostrarResumen(); // Muestra el resumen de la reserva realizada
        System.out.println(""); // Imprime una línea en blanco

        System.out.println("¡Gracias por su compra, " + cliente.getNombre() + " " + cliente.getApellido() + "! Disfrute la funcion!"); // Muestra un mensaje al cliente por su compra, mostrando su nombre
    }
}
