// Siempre que no usemos la sintaxis de funcion flecha, podemos aplicar el concepto de Hoisting

let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log("El resultado de la suma es: ", respuesta);

function sumarTodo(){
    let suma = 0;
    for(const element of arguments){
        suma += element; //Arguments es para arreglos
    }
    return suma;
}