// Parametros: lista de variables que definimos en una funcion
// Argumentos: valores que pasamos cuando llamamos a la funcion

// Una funcion se puede definir, tambien, como OBJETO, por lo cual tiene una 
// propiedad llamada 'arguments'.

// arguments: es un array, sirve para poder acceder a los diferentes valores de los 
// parametros.


// Funcion tipo expresion
let sumar = function(a, b){
    console.log(arguments[0]); // Muestra el parametro de 'a', no de 'b'
    console.log(arguments[1]); // Muestra el parametro de 'b'
    console.log(arguments[2]);
    
    return a + b + arguments[2];
}
resultado = sumar(3, 5, 9);   // JS es flexible al dejar agregar argumentos
console.log(resultado);


// Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);

function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i];  // 'arguments' es para arreglos
    }
    return suma;
}