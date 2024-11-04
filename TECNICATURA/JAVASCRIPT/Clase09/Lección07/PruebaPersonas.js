class Persona{
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++ Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona(){
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

    set edad(edad){
        this._edad = edad;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    toString(){
        return `Id Persona numero: ${this._idPersona}, Nombre: ${this._nombre}, Apellido: ${this._apellido}, Edad: ${this._edad}`;
    }
}

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

class Cliente extends Persona {
    static contadorCliente = 0;

constructor(nombre, apellido, edad, fechaRegistro) {
    super(nombre, apellido, edad);
    this._idCliente = ++Cliente.contadorCliente;
    this._fechaRegistro = fechaRegistro;
}
    
    // Getter para idCliente
    get idCliente() {
        return this._idCliente;
    }
    
    // Getter para fechaRegistro
    get fechaRegistro() {
        return this._fechaRegistro;
    }
    
    // Setter para fechaRegistro
    set fechaRegistro(nuevaFecha) {
        this._fechaRegistro = nuevaFecha;
    }
    
    // Método toString
    toString() {
        return `${super.toString()}, Cliente ID: ${this._idCliente}, Fecha de Registro: ${this._fechaRegistro}`;
    }
}

//Prueba Clase Persona
let persona1 = new Persona("Leonardo", "Guerra", 41);
console.log(persona1.toString());

let persona2 = new Persona("Ana", "Garin", 39);
console.log(persona2.toString());
console.log();

//Prueba Clase Empleado
let empleado1 = new Empleado("Nelson", "Rios", 44, 2000000);
console.log(empleado1.toString());

let empleado2 = new Empleado("Nazareno", "Castro", 23, 500000);
console.log(empleado2.toString());
console.log();

//Prueba Clase Cliente
let cliente1 = new Cliente("Andés", "Toledo", 49, new Date());
console.log(cliente1.toString());

let cliente2 = new Cliente("Hilda", "Guerra", 53, new Date());
console.log(cliente2.toString());