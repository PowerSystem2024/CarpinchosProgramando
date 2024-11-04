// Una funcion es un codigo que realiza una tarea y se puede reutilizar.

// HOISTING: "del inglés: elevación" Independientemente de dónde se declare una variable o una función, en tiempo de ejecución JavaScript las reconocerá antes de llegar a la línea donde se declaran. Esto significa que se puede acceder a la variable antes de su declaración, pero su valor será undefined hasta que la inicialización se ejecute.

miFuncion(8,2) // Js reconoce la funcion y su comportamiento. Esto se conoce como hoisting

function miFuncion(a, b){
    return a + b;
    // Si una función no tiene una declaración de return, o si se usa return sin un valor, la función devuelve implícitamente undefined. No es necesario que escribir return undefined; JavaScript lo hace automáticamente.
}

// Llamamos a la funcion
miFuncion(5, 4);
let resultado = miFuncion(6,7);
console.log(resultado);