// while

let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");


// do while

let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);

console.log("Fin del ciclo do while")



// for

for( let contando = 0; contando < 3; contando++ ){
    console.log(contando);
}
console.log("Fin del ciclo for");



// Palabra reservada break. Rompe cualquiera sea la estructura

for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break;  // solo va a mostrar el primer numero par
    }
}
console.log("Termina el ciclo al encontrar el primer numero par");


// Continue

for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue;  // ir a la siguiente iteracion
    }
    console.log(contando);
}
console.log("Termina el ciclo");



// Etiquetas Labels

inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio;  //  tambien puede usarse con break o continue
    }
    console.log(contando);
}
console.log("Termina el ciclo");
