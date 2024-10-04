class Persona { // CLASE PADRE
    constructor(nombre,apellido,edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    // GETTERS Y SETTERS
    get nombre() {
        return this._nombre
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    // EJERCICIO
    get apellido() {
        return this._apellido
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
}

class Empleado extends Persona { // CLASE HIJA, HEREDA DE PERSONA 
    constructor(nombre,apellido,edad,departamento) {
        super(nombre,apellido,edad);
        this._departamento = departamento;
    }
    get departamento() {
        return this._departamento
    }
    set departamento(departamento) {
        this._departamento = departamento;
    }
}

// Crear el método get y set para el atributo de apellido, luego modificar el apellido a través del  set y 
// mostrar con un console.log lo que es el get donde muestra el resultado obtenido.

let persona1 = new Persona("Wanda", "Lanatta", 24);
let persona2 = new Persona("Samira", "Lopez", 40);

persona1.apellido = "CAMBIOAPELLIDO"
console.log(persona1.apellido);

let empleado1 = new Empleado("Fernando","Simich",38,"1C");
console.log(empleado1)