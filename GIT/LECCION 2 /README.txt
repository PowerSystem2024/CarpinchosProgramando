CLASE 02 MIÉRCOLES 21 DE AGOSTO DEL 2024 - Portafolio 2

Vamos a cargar la llave SSH publica en GitHub

Para copiar la llave publica debes ir al archivo .ssh y allí encontrarás el archivo .pub lo podes abrir con el txt, luego copiar el contenido que esta dentro.
1- copiar la llave publica. Ir a GitHub, vamos a setting, vamos a SSH and GPG keys
2- crear una nueva #New SSH key poner nombre y pegar la ssh publica, con esto esta listo.

Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.
git branch #Vemos en que rama estamos

git checkout master #Ponernos en la rama master

git branch -M main #Cambiamos el nombre a la rama master

git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo

git remote -v #Vemos si ya esta conectado

git merge segunda #Mergeamos lo que tenemos en la rama segunda en main

git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy

git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.

Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.