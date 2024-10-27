package capybarafilms.domain.entities;

import capybarafilms.domain.entities.types.TipoButaca; // Importamos el tipo de butaca (común o premium)
import capybarafilms.domain.entities.types.Ubicacion;

public class Sala {

    // Definimos atributos "final" ya que son constantes y no se pueden modificar
    private final Butaca[][] butacas; // Matriz de butacas en la sala
    private final int capacidad = 12; // La capacidad de la sala es de 12 filas y 12 butacas por fila
    private final int minPremium = 5; // Las butacas son premium desde la fila 5
    private final int maxPremium = 7; // Las butacas son premium hasta la fila 7
    private final Pelicula pelicula; // Cada sala proyecta una película

    // Constructor que inicializa la sala con una película
    public Sala(Pelicula pelicula) {
        this.pelicula = pelicula; // Asigna la película a la sala
        this.butacas = new Butaca[capacidad][capacidad]; // Crea la matriz de butacas
        llenarButacas(); // Llama al método para llenar las butacas
    }

    // Método que llena las butacas de la sala
    private void llenarButacas() {
        for (var fila = 0; fila < capacidad; fila++) {
            for (var butaca = 0; butaca < capacidad; butaca++) {
                if (fila >= minPremium && fila <= maxPremium) {
                    // Crea una butaca premium
                    butacas[fila][butaca] = new Butaca(TipoButaca.PREMIUM, new Ubicacion(fila, butaca));
                } else {
                    // Crea una butaca común
                    butacas[fila][butaca] = new Butaca(TipoButaca.COMUN, new Ubicacion(fila, butaca));
                }
            }
        }
    }

    // Método para asignar una butaca a una ubicación específica
    public void asignarButaca(Ubicacion ubicacion) {
        if (ubicacion.getFila() >= 0 && ubicacion.getFila() < butacas.length
                && ubicacion.getButaca() >= 0 && ubicacion.getButaca() < butacas[ubicacion.getFila()].length) {
            Butaca butaca = butacas[ubicacion.getFila()][ubicacion.getButaca()];
            if (!butaca.isEstado()) {
                butaca.setEstado(true); // Marca la butaca como ocupada
            } else {
                System.out.println("La butaca se encuentra ocupada."); // Informa si ya está ocupada
            }
        } else {
            System.out.println("Fila o butaca inválidos."); // Mensaje de error si son inválidos
        }
    }

    // Método que calcula el precio de la entrada según la ubicación
    public double precioDeEntrada(Ubicacion ubicacion) {
        // Verifica que se esté accediendo a una posición válida en la matriz de butacas
        if (ubicacion.getFila() >= 0 && ubicacion.getFila() < butacas.length
                && ubicacion.getButaca() >= 0 && ubicacion.getButaca() < butacas[ubicacion.getFila()].length) {
            return butacas[ubicacion.getFila()][ubicacion.getButaca()].getCategoria().getPrecio() 
                   + pelicula.getFormato().getPrecioExtra(); // Devuelve el precio de la butaca más el extra por el formato de la película
        } else {
            System.out.println("Fila o butaca inválidos."); // Mensaje de error si la posición es inválida
            return 0; // Devuelve 0 si hay un error
        }
    }

    // Método que verifica si una butaca está ocupada
    public boolean butacaEstaOcupada(Ubicacion ubicacion) {
        return butacas[ubicacion.getFila()][ubicacion.getButaca()].isEstado(); // Retorna el estado de la butaca
    }

    // Método que devuelve una butaca según su ubicación
    public Butaca getButaca(Ubicacion ubicacion) {
        return butacas[ubicacion.getFila()][ubicacion.getButaca()]; // Devuelve la butaca correspondiente
    }

    // Método que devuelve la capacidad de la sala
    public int getCapacidad() {
        return capacidad; // Devuelve la capacidad de filas y columnas
    }

    // Método que devuelve una representación en texto de la sala
    @Override
    public String toString() {
        String resultado = "Sala N° 1\n"; // Inicia la cadena con un mensaje sobre la sala
        resultado += "Película: " + pelicula.getNombre() + "\nFormato de la película: " + pelicula.getFormato() 
                + "\nGénero de la pelicula: " + pelicula.getGenero() + "\n" + "Duración: " + pelicula.getDuracion() + " min." 
                + "\nDirigida por: " + pelicula.getDirector() + "\n\nButacas Seleccionadas: \n"; // Agrega el título, formato, genero, duracion y director de la película
             // Recorre las filas de la sala
            for (int fila = 0; fila < capacidad; fila++) {
            // Recorre las butacas en cada fila
            for (int butaca = 0; butaca < capacidad; butaca++) {
                Butaca b = butacas[fila][butaca]; // Obtiene la butaca actual
                // Agrega un símbolo dependiendo del estado de la butaca
                if (b.isEstado()) {
                    resultado += "[X]"; // Ocupada
                } else {
                    resultado += "[ ]"; // Disponible
                }
            }
            resultado += "\n"; // Salto de línea al final de cada fila
        }
        return resultado; // Devuelve el mensaje final
    }
}