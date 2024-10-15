package Domain;
import java.util.Date;

public class Cliente extends Persona{
    private int idCliente;
    private static int idClienteContador;
    private Date fechaRegistro;
    private boolean vip;

    public Cliente(Date fechaRegistro,boolean vip,String nombre,char genero,int edad,String direccion) {
        super(nombre,genero,edad,direccion);
        this.idCliente = ++Cliente.idClienteContador;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    public int getIdCliente() {
        return this.idCliente;
    }
    public Date getFechaRegistro() {
        return fechaRegistro;
    }
    public void setFechaRegistro(Date fech) {
        fechaRegistro = fech;
    }
    public boolean isVip(){
        return this.vip;
    }
    public void setVip(boolean bool){
        this.vip = bool;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("idCliente=").append(idCliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
}