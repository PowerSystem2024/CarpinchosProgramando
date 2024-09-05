// Paso por valor: es cuando utilizamos tipos que no son objetos, ej: tipo numerico
// tipo booleano, etc.

// Tipos primitivos
let k = 10;     // esta variable no sufre ningun cambio, por mas que la mandemos como argumentos a la funcion.
function cambiarValor(a){ // Paso por valor
    a = 20;
}
cambiarValor(k);    // Aqui le estamos enviando a la funcion una copia del valor de k(10)
// No le decimos que modifique el valor de k al ingresar a la funcion

console.log(k);