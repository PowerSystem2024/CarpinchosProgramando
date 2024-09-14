for(let contador = 0; contador < 3; contador ++){
console.log(contador);
}
console.log("Fin del ciclo FOR");

console.log("\nComo trabaja BREAK: ");
for (let contador = 0; contador <= 10; contador ++){
    if(contador % 2 == 0){
        console.log(contador);
        break; // Encuentra el primer numero par y detiene la iteración.
    }
}
console.log("Termina el ciclo al encontrar los numeros pares.");


console.log("\nUsando CONTINUE y LABELS: ");
inicio:
for(let contador = 0; contador <= 10; contador ++){
    if(contador % 2!== 0){
        break inicio;   // Continua la iteración.
    }
    console.log(contador);
}
console.log("Termina el ciclo For usando continue y labels.");