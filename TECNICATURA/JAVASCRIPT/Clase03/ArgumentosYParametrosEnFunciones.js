function miFuncion(a, b){ // <-- PARAMETRO (VARIABLES)
    console.log("El resultado de la suma es: ", a + b);
}

miFuncion(3, 3); // <-- ARGUMENTO (VALOR REAL)

// Funcion del tipo expresión:
let sumar = function(a, b){
    console.log(arguments[0]); // Muestra el argumento del parámetro a
    console.log(arguments[1]); // Muestra el argumento del parámetro b
    console.log(arguments[2]); // Aunque no este declarado el tercer parámetro JS es flexible y permite como Undefined.
    return a + b + arguments[2];
}

let resultado = sumar(3, 2, 9);
console.log(resultado);