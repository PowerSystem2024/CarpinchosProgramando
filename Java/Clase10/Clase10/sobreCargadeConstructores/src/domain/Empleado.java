package domain;

public class Empleado extends Persona {// Java solamente usamos jerarquía de clase simple

    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleado;// Es para incrementar

    //Constructores
    public Empleado() { // Constructor1
        this.idEmpleado = ++Empleado.contadorEmpleado;
    }

    public Empleado(String nombre, double sueldo) { //Constructor2
        //super(nombre);
        this(); //Estamos llamando desde aquí al constructor vacío (llamar a un constructor interno)
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

}
