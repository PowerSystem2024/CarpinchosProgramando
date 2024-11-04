package domain;

import java.util.Date;

public class Cliente extends Persona {
    // Atributos
    private int idCliente; // Identificador único del cliente
    private Date fechaRegistro; // Fecha en que el cliente se registró
    private boolean vip; // Indica si el cliente es VIP (true/false)
    private static int contadorClientes; // Atributo estático para generar idCliente únicos

    // Constructor
    public Cliente(Date fechaRegistro, boolean vip, String nombre, char genero, int edad, String direccion) {
        super(nombre, genero, edad, direccion); // Llamada al constructor de la superclase Persona
        this.idCliente = ++Cliente.contadorClientes; // Incrementa y asigna el idCliente
        this.fechaRegistro = fechaRegistro; // Asigna la fecha de registro
        this.vip = vip; // Asigna si el cliente es VIP o no
    }    

    // Getter para obtener el id del cliente
    public int getIdCliente() {
        return this.idCliente;
    }

    // Getter para obtener la fecha de registro del cliente
    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    // Getter para verificar si el cliente es VIP
    public boolean isVip() {
        return this.vip;
    }

    // Setter para modificar la fecha de registro del cliente
    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    // Setter para establecer si el cliente es VIP o no
    public void setVip(boolean vip) {
        this.vip = vip;
    }

    // Sobrescribe el método toString para imprimir los detalles del cliente
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(); // Usa StringBuilder para crear la cadena
        sb.append("Cliente ");
        sb.append("idCliente: ").append(idCliente); // Agrega el id del cliente
        sb.append("\nfechaRegistro: ").append(fechaRegistro); // Agrega la fecha de registro
        sb.append("\nvip: ").append(vip); // Agrega el estado VIP
        sb.append("\n").append(super.toString()); // Incluye los detalles de la clase Persona
        return sb.toString(); // Retorna la cadena con los detalles del cliente
    }
}
