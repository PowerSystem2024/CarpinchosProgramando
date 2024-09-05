// Funciones de tipo self e invoking
// No la podemos reutilizar

(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6); // aqui se llama asi misma.

// ---------------------------------------------------------------

// Podemos ver que tipo de dato es
function miFuncion(a, b){
    console.log("Sumamos: "+ (a + b));
}

console.log(typeof miFuncion); // Con 'typeof' podemos ve rel tipo de dato.


// Para saber cuantos argumentos se han definido en la funcion.
// 'arguments' debe estar dentro de la funcion.
function miFuncionDos(a, b){
    console.log(arguments);
    console.log(arguments.length)
}

miFuncionDos(5, 7);

// toString: convierte nuestra funcion a texto
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);