let persona = { //Se crea el objeto persona
    nombre: "Carlos", // Atributos
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: "ES",
    get language(){
        return this.idioma.toUpperCase(); // toUpperCase convierte el string a mayusculas
    },
    set language(lenguaje){
        this.idioma = lenguaje.toUpperCase();
    },
    nombreCompleto: function(){ //metodo o funcion
        return this.nombre+" "+this.apellido;
    },
    get nombreYEdad(){ //Metodo get, en este caso va a mostrar nombre y edad.
        return this.nombre + ", Edad: "+ this.edad;
    }
}

console.log("Comenzamos con el metodo get: ");
console.log(persona.nombreYEdad);
console.log("Comenzamos con el metodo get y set para idiomas: ");
persona.language = "en";
console.log(persona.language);

console.log("\n----- CONSTRUCTOR -----");
function Persona1(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){ // Metodo para mostrar nombre completo
        return this.nombre + " "+this.apellido;
    }
}
let padre = new Persona1("Leo", "Lopez", "leo@mail.com");
padre.nombre = "Luis"; //Modificamos el nombre
padre.telefono = "1131313131"; // Propiedad exclusiva del objeto "padre".
console.log(padre);
console.log(padre.nombreCompleto()); // Invocamos al metodo para mostrar nombre completo

let madre = new Persona1("Laura", "Contrera", "lauc@mail.com");
console.log(madre);
console.log(madre.nombreCompleto());
//console.log(madre.telefono); // La propiedad no esta definida


console.log("----- DIFERENTES FORMAS DE CREAR OBJETOS ------");
// Caso Objeto 1
let miObjeto = new Object(); // Esta es la opcion formal.
// Caso Objeto 2
let miObjeto1 = {}; // Esta opcion es breve y recomendada.

// Caso String 1
//let miCadena = new String("Hola"); // Sintaxis formal.
// Caso String 2
let miCadena2 = "Hola"; // Sintaxis simplificada y recomendada.

// Caso con números 1
//let miNumero = new Number(1); //Sintaxis formal
// Caso con números 2
let miNumero1 = 1; // Sintaxis recomendada

// Caso boolean 1
//let miBoolean = new Boolean(false); // formal.
// Caso boolean 2
let miBoolean1 = false; // Sintaxis recomendada.

// Caso Arreglos 1
let miArreglo = new Array(); // formal.
// Caso Arreglos 2
let miArreglo1 = []; // Recomendada.

// Caso Funcion 1
let miFuncion = new function(){}; // Despues de new, lo que sigue se considera un objeto
// Caso Funcion 2
//let miFuncion1 = function(){}; // Notacion simplificada y recomendada.

// Uso de prototype:
//Si utilizamos una variable que almacena la referencia de un objeto, y si agregamos una nueva propiedad o nuevos metodos se asocia unicamente a la referencia del objeto que almacena esta variable. Esto significa que cualquier instancia creada a partir de esa función constructora tendrá acceso a esos métodos y propiedades a través de la cadena de prototipos.
console.log("\n--- PROTOTYPE ---");

Persona1.prototype.telefono = "1131353235"
console.log(padre);
console.log(" Nueva caracteristica usando prototype: ",madre.telefono);

//Uso de Call: Pasa arguemntos uno a uno
console.log("\n--- CALL ---");
let persona2 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.apellido+" "+telefono;
        //return this.nombre+" "+this.apellido;
    }
}

let persona3 = {
    nombre: "Carlos",
    apellido: "Lara"
}

console.log(persona2.nombreCompleto2("Lic. ", "5469853215"));
console.log(persona2.nombreCompleto2.call(persona3, "Ing. ", "543814056231"));

// Apply: Pasa un array de argumentos
console.log("\n --- APPLY --- ");
let arreglo = ["Ing. ", "543814051245"]
console.log(persona2.nombreCompleto2.apply(persona3, arreglo));