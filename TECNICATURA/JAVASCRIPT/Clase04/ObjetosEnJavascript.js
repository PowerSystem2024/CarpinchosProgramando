let x = 10; // Variable de tipo primitiva
console.log(x.lenght); // indefinido porque no es un objeto

//Objeto
console.log("\nPrimer objeto:");

let persona = { //Se crea el objeto persona
    nombre: "Carlos", // Atributos
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function(){ //metodo o funcion
        return this.nombre+" "+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

console.log("\nSegundo objeto:");
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "1165983265"
console.log(persona2.telefono);

console.log("\n",persona["apellido"]); // Se accede como si fuera un arreglo
for(let propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

persona.apellido = "Betancud"; // Cambiamos dinamicamente el valor de un onbjeto
console.log(persona);

persona.apellida = "Betancud"; // agregamos erronamente una propiedad
console.log("\n",persona);
delete persona.apellida; // borramos el error
console.log("\n",persona);

console.log("\nDistintas formas de imprimir un objeto: ");
//Concatenar
console.log("\n1. Concatenando: ----------\n",persona.nombre+" "+persona.apellido);

console.log("\n2. Ciclo for in: ---------\n");
for(let nombrePopiedad in persona){
    console.log(persona[nombrePopiedad]);
}

console.log("\n3. Con la funcion Object.values(): ------\n");
let personaArray = Object.values(persona);
console.log(personaArray);

console.log("\n4. Con el metodo JSON.stringify: ------\n");
let personaString = JSON.stringify(persona);
console.log(personaString);
