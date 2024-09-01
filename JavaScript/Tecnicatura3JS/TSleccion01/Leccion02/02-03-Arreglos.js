
//let autos = new Array("ferrari","Renault","BNW");
//esta es la sintaxia vieja 
const autos=["ferrari","Renault","BMw"];

console.log(autos);
console.log(autos[0]);
console.log(autos[2]);
for(let i = 0; i  <+ " " +autos.length; i++) {



    console.log(autos[i]);     
}
// Modificamos los elementos del arreglo
autos[0] = 'Volvo';

// Agregamos nuevos valores al arreglo
autos.push('Audi'); // Agregamos el elemento al final del arreglo

console.log(autos); // []

// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';

console.log(autos); // []

// Tercera forma de agregar elementos teniendo CUIDADO

autos[6] = 'Renault';

console.log(autos); // []
// Cómo preguntar si es un Array o Arreglo
console.log(Array.isArray(autos)); // Devuelve un booleano

console.log(autos instanceof Array); // Preguntamos si la variable es una instancia de la clase Array
