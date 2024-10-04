let x = 10; // variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos')

// objeto
let persona= {
    nombre: 'Wanda',
    apellido: ' Lanatta,
    Email: 'wandalanatta@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); // convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma =lang.toUpperCase();
    },
    nombreCompleto: function(){// metodo o funcoin en Javascript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ // este es el metodo get
        return ' El Nombre es: '+ this.nombre+' edad: '+this.edad;    
    }
    
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

let persona2 = new Object(); // debe crear un nuevo objeto en memoria
persona2.nombre = ' Maxi';
persona2.direccion = 'Valeria del Mar';
persona2.telefono = '011666106123'
console.log(persona2.telefono);
console.log('creamos un nuevo objeto');

console.log(persona['apellido']); // accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');

// for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('cambiamos y eliminamos un error')
persona.apellida = 'Montenegro';// cambiamos dinamicamente un valor del objeto
delete persona.apellida ; 
console.log(persona);

// distintas formas de imprimir un objeto
// numero 1 : la mas sencilla : concatenar cada valor de cada propiedad
console.log('Distinta formas de imprimir un objeto: forma1');
console.log(persona.nombre+', '+persona.apellido);

// Numero 2: A travez del ciclo for in
console.log('distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

// numero 3: La funcion Objets.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Numero 4: Utilizamos el metodo JSON.Stringify
console.log('Distintas formas de imprimir un objeto: forma 4')
let personaString = JSON.stringify(persona);
console.log(personaString);
