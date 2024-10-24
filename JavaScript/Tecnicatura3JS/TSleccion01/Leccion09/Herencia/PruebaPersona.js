class Persona {

    static contadorPersona = 0;

    constructor(nombre,apellido,edad) {
        this._idPersona = ++Persona.contadorPersona;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona() {
        return this._idPersona;
    }

    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }
    get edad(){
        return this._edad;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    set edad(edad){
        this._edad = edad;
    }

    toString(){
        return this._idPersona + " " + this._nombre + " " + this._apellido + " " + this._edad;
    }
}

class Empleado extends Persona {

    static contadorEmpleado = 0;

    constructor(nombre,apellido,edad,sueldo) {
        super(nombre,apellido,edad);
        this._idEmpleado = ++Empleado.contadorEmpleado;
        this._sueldo = sueldo;
    }

    get idEmpleado() {
        return this._idEmpleado;
    }
    get sueldo(){
        return this._sueldo
    }
    set sueldo(sueldo){
        this._sueldo = sueldo
    }

    toString(){
        return super.toString() + " " +  this._idEmpleado + " " + this._sueldo;
    }
    
}

class Cliente extends Persona {

    static contadorCliente = 0;

    constructor(nombre,apellido,edad,fechaRegistro) {
        super(nombre,apellido,edad);
        this._idCliente = ++Cliente.contadorCliente;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente() {
        return this._idCliente;
    }
    get fechaRegistro(){
        return this._fechaRegistro
    }
    set fechaRegistro(fechaRegistro){
        this._fechaRegistro = fechaRegistro
    }

    toString(){
        return super.toString() + " " +  this._idCliente + " " + this._fechaRegistro;
    }
    
}

// PRUEBA PERSONA

let persona1 = new Persona("Liliana","Murguia",32)
console.log(persona1.toString());

// PRUEBA EMPLEADO

let empleado1 = new Empleado("Empleado","emp1",22,2050000)
console.log(empleado1.toString());

// PRUEBA CLIENTE

let cliente1 = new Cliente("Clientito","client1",44, new Date())
console.log(cliente1.toString()); 