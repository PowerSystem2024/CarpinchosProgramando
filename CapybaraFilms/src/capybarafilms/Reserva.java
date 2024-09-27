package capybarafilms;

import java.util.Date;

public class Reserva {

    private Date fecha;
    private Butaca butaca;
    private Pelicula pelicula;
    private Sala sala;
    private Candy candy;
    private Cliente cliente;
    private boolean estado;

    public Reserva(Date fecha, Butaca butaca, Pelicula pelicula, Sala sala, Candy candy, Cliente cliente, boolean estado) {
        this.fecha = fecha;
        this.butaca = butaca;
        this.pelicula = pelicula;
        this.sala = sala;
        this.candy = candy;
        this.cliente = cliente;
        this.estado = estado;
    }

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    public Butaca getButaca() {
        return butaca;
    }

    public void setButaca(Butaca butaca) {
        this.butaca = butaca;
    }

    public Pelicula getPelicula() {
        return pelicula;
    }

    public void setPelicula(Pelicula pelicula) {
        this.pelicula = pelicula;
    }

    public Sala getSala() {
        return sala;
    }

    public void setSala(Sala sala) {
        this.sala = sala;
    }

    public Candy getCandy() {
        return candy;
    }

    public void setCandy(Candy candy) {
        this.candy = candy;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public boolean isEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    @Override
    public String toString() {
        return "Reserva: " + "fecha: " + fecha + ", butaca: " + butaca + ", pelicula: " + pelicula + ", sala: " + sala + ", candy: " + candy + ", cliente: " + cliente + ", estado: " + estado;
    }
}