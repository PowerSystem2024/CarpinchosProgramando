// Las funciones flecha fueron introducidas con la especificación ECMAScript 6 (ES6).
// La sintaxis de las funciones flecha permite omitir la palabra clave function, las llaves {} y la palabra reservada Return si la función tiene una sola expresión que se devuelve automáticamente.
// Las funciones flecha no tienen el objeto arguments que las funciones tradicionales tienen.

const sumarFuncionFlecha = (a, b) => a + b;
let resultado = sumarFuncionFlecha(3, 7) // Asignamos el valor a una variable.
console.log(resultado);