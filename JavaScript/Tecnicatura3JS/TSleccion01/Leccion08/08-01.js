// NO SE PUEDE PORQ ANTES HAY Q CREAR LA CLASE
// let perosna3 = new Persona("Carlos","Joyst",66)

class Persona { // CLASE PADRE

    static contadorPersonas = 0; // Atributo estatico
    //email = "Valor default email"; // Atributo NO estatico

    static get MAX_OBJ() { // Este metodo simula una constante
        return 4;
    }

    constructor(nombre,apellido,edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        if(Persona.contadorPersonas < Persona.MAX_OBJ) {
            Persona.contadorPersonas++;
            this.idPersona = Persona.contadorPersonas;
        } else {
            console.log("Se supero el maximo de objetos")
        }
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

    nombreCompleto() {
        return this.idPersona + " " + this.nombre + " " + this.apellido
    }
    toString() {
        return this.nombreCompleto();
    }
    // STATIC
    static saludar() {
        console.log("saludo desde el metodo static")
    }
    static saludar2(persona) {
        console.log("HOLA " + persona.nombre + " " + persona.apellido);
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

    // Sobreescribo el metodo de la clase Padre (Persona)
    nombreCompleto() {
        return super.nombreCompleto() + ", " + this._departamento
    }
}

// Crear el método get y set para el atributo de apellido, luego modificar el apellido a través del  set y 
// mostrar con un console.log lo que es el get donde muestra el resultado obtenido.

let persona1 = new Persona("Wamda", "Lanatta", 24);
let persona2 = new Persona("Fernando", "Simich", 40);

persona1.apellido = "CAMBIOAPELLIDO"
console.log(persona1.apellido);

let empleado1 = new Empleado("Jose","Perez",35,"1C");
console.log(empleado1.nombreCompleto())

// Object.prototype.toString Manera de acceder a atributos y metodos de forma dinamica
console.log(persona1.toString())
console.log(persona2.toString())
console.log(empleado1.toString())

// No se puede desde el OBJETO
//persona1.saludar();
// TIENE Q SER DESDE LA CLASE
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorPersonas);
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);

let persona3 = new Persona("Wanda", "Lanatta", 24);
let persona4 = new Persona("Fernando", "Simich", 40);