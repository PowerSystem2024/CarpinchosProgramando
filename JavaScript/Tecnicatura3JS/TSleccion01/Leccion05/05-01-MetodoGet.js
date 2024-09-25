
console.log('Comenzamos a utilizar el metodo get')
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email ){// constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre +' '+ this.apellido
    }

}
let padre = new Persona3('Natalia', 'Conti', 'wandalanatta@gmail.com'); 
padre.nombre = 'Luis'; // modificamos el nombre
padre.telefono = '112211334433'; // una propiedad esclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); // utilizamos la funcion
let madre = new Persona3('Micaela', 'Perez', ' MicaelaPerez@gmail.com');
console.log(madre);
console.log(madre.telefono);// la propiedad no esta definida
console.log(madre.nombreCompleto());

// diferentes formas de crear objetos 
// Caso objeto 1
let miObjeto = new Object(); //Esta es una opcion formal
// caso objeto 2
let miObjeto2 = {}; // esta opcion es breve y recomendada

// caso string 1
let miCadena1 = new String('Hola'); // sintaxis formal
// caso String 2
let miCadena2 = 'Hola';//Esta es la sintaxis simplificada y recomendada

// cvaso con numeros 1
let miNumero = new Number(1);// es formal no recomendable
// caso con numeros 2
let miNumero2 = 1;// sintaxis recomendada

// caso boolean 1
let miBoolean1 = new Boolean(false);// Formal
// caso boolean 2
let miBoolean2 = false; // sintaxis recomendada

// caso arreglos 1
let miArreglo1 = new Array(); // formal
// caso arreglos 2
let miArreglo2 = [];// sintaxis recomendada

// caso function 1
let miFuncion1 = new function(){}; //todo despues de new es considerado objeto
// caso function 2
let miFuncion2 = function(){};// notacion simplificada y recomendada

// uso de prototype
Persona3.prototype.telefono = '1133146155';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '264554434345'
console.log(madre.telefono);

// uso de call
let persona4 ={
    nombre: 'Angel',
    apellido: ' Dimaria',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
       //return this.nombre+' '+this.apellido;
    }
}

let persona5 ={
    nombre: 'Lionel',
    apellido: 'Messi'
}

console.log(persona4.nombreCompleto2('Lic.', '261111111'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '261444444'));

// metodo apply
let arreglo = ['Ing.', '2612313132']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));