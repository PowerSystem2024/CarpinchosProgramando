// CTRL + SHIFT + P para inciar el QUOKKA
// --- CREACION DE ARRAY O ARREGLOS ---

// Forma antigua de declarar arreglo (ya no se recomienda)
// let autos = new Array('Ferrari', 'Renault', 'BMW');  

// Esta es la nueva sintaxis para declarar arreglo
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);


// --- RECORREMOS LOS ELEMENTOS DE UN ARRREGLO ---
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){      // '.length' nos va a mostrar el numero del arreglo, cuantas posiciones tiene.
    console.log(i+': '+autos[i]);
}  



// --- MODIFICAMOS LOS ELEMENTOS DEL ARREGLO ---
autos[1] = 'Volvo';
console.log(autos[1]);



// --- AGREGAR NUEVOS VALORES AL ARRAY ---
autos.push('Audi');       // El elemento se agrega al final
console.log(autos);

// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

// Tercera forma de agregar elementos teniendo CUIDADO
autos[6] = 'Renault';
console.log(autos);     // quedan espacios vacios ocupando memoria, CUIDADO.



// --- COMO PREGUNTAR SI ES UN ARRAY ---
console.log(Array.isArray(autos));

console.log(autos instanceof Array);