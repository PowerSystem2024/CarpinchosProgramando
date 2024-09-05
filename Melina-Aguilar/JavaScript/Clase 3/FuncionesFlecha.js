// --- Funciones flecha ---
// similar a la funcion expresion o anonima
// Cuando utilizamos funciones flecha ya no es necesario utilizar la palabra 'function'
// Simplemente pedimos los parametros. Tampoco es necesario usar 'return' ni {}.
// Luego de => cuerpo de la funcion

const sumarFuncionFlecha = (a, b) => a + b; // 'const' ya no se puede cambiar el valor que se le ha asignado
resultado = sumarFuncionFlecha(3, 7);  // Asignamos el valor a una variable
console.log(resultado);