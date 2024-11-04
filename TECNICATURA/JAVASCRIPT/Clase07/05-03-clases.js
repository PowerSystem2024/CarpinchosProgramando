//let persona3 = new Persona('Carla', 'Ponce'); //esto no se debe hacer: Persona is not defined

class Persona{ //clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
    //Sobreescribiendo el método de la clase padre (Object)
    toString(){ //regresa un string
        //se aplica el polimorfismo que significa = múltiples formas en tiempo de ejecución
        //el método que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this.departamento = departamento;
    }

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }
}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado('María', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString //esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());
console.log(persona1.toString()); //Polimorfismo

