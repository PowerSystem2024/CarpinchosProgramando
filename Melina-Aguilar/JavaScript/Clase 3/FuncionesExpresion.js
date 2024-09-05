// Declaramos una funcion de tipo expresion o anonima. 
// Va en una sola linea por lo tanto necesita ';'

let x = function(a, b){ return a + b}; // le asignamos a 'x' la funcion
resultado = x(5, 6);  // al llamarla se pone la variable (a la que le asignamos la funcion) y parentesis
console.log(resultado);