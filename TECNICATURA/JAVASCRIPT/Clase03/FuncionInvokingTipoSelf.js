// Funciones de tipo Self o Invoking porque se llaman a si mismas.
(function(a, b){ //No es reutilizable
    console.log("Ejecutando la funcion: " + (a + b));
})(9,6); //Se llama asi misma y es una función anónima