class Empleado extends Persona {
    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo) {
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }

    // Getter para idEmpleado
    get idEmpleado() {
        return this._idEmpleado;
    }

    // Getter para sueldo
    get sueldo() {
        return this._sueldo;
    }

    // Setter para sueldo
    set sueldo(nuevoSueldo) {
        if (nuevoSueldo >= 0) {
            this._sueldo = nuevoSueldo;
        } else {
            console.log("El sueldo no puede ser negativo.");
        }
    }

    // Método toString
    toString() {
        return `${super.toString()}, Empleado ID: ${this._idEmpleado}, Sueldo: ${this._sueldo}`;
    }
}