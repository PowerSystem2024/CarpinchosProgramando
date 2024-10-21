package capybarafilms.domain.entities;

import capybarafilms.domain.entities.types.TipoButaca; // Importamos el tipo de butaca
import capybarafilms.domain.entities.types.Ubicacion; // Importamos la clase que indica la ubicación de la butaca

public class Butaca {

    private Ubicacion ubicacion; // Dónde está la butaca (fila y número).
    private final TipoButaca categoria; // Tipo de butaca: común o premium.
    boolean estado; // Indica si la butaca está ocupada (true) o libre (false).

    // Constructor para crear una nueva butaca.
    public Butaca(TipoButaca categoria, Ubicacion ubicacion) {
        this.categoria = categoria; // Se asigna el tipo de butaca.
        this.estado = false; // Al principio, la butaca está libre.
        this.ubicacion = ubicacion; // Se asigna la ubicación de la butaca.
    }

    // Cambia el estado de la butaca.
    public void setEstado(boolean estado) {
        this.estado = estado; // Se actualiza el estado de la butaca.
    }

    // Devuelve el tipo de butaca (común o premium).
    public TipoButaca getCategoria() {
        return categoria; // Se devuelve el tipo de butaca.
    }

    // Verifica si la butaca está ocupada.
    public boolean isEstado() {
        return estado; // Se devuelve el estado de la butaca.
    }

    // Devuelve la ubicación de la butaca.
    public Ubicacion getUbicacion() {
        return ubicacion; // Se devuelve la ubicación de la butaca.
    }

    // Cambia la ubicación de la butaca.
    public void setUbicacion(Ubicacion ubicacion) {
        this.ubicacion = ubicacion; // Se actualiza la ubicación de la butaca.
    }

}
