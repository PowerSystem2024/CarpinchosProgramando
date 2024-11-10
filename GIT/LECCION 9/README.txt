CLASE 09 MIÉRCOLES 9 DE OCTUBRE DEL 2024 - Portafolio 9
Tarea para antes de las 23 horas: Investigar como se puede clonar un repo con el https del mismo, ósea siendo ustedes los dueños del repositorio, y desde la nube quieren traer este repo a nuestro ordenador, nos pedira Username y password: ¿qué se debe hacer para lograr hacer cambios y así utilizar pull, push, y todo lo necesario para trabajar?. Como referencia les digo que solo usuario y contraseña no será suficiente, esto cambio desde el año 2021 y ahora hay algo más para poder hacer esto y tener así acceso total.

Configurar múltiples colaboradores en un repositorio de GitHub
Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits, ni ramas. Esto quiere decir que pueden copiar tu proyecto pero no colaborar con él, si este es publico, de otra manera, osea, si es privado es necesario que realmente estes haciendo una invitación, sino no lo van a poder ver. Existen varias formas de solucionar esto para poder aceptar contribuciones. Una de ellas es añadir a cada persona de nuestro equipo como colaborador de nuestro repositorio.

Cómo agregar colaboradores en Github Solo debemos entrar a la configuración de colaboradores de nuestro proyecto. Se encuentra en:

Repositorio > Settings > Collaborators
Ahí, debemos añadir el email o username de los nuevos colaboradores.

Si, como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar de la siguiente manera:

Hacer un commit con el nuevo mensaje que queremos, esto nos abre el editor de texto de la terminal:

git commit —amend #Corregimos el mensaje
git pull origin main #Traer el repositorio remoto
git push --set-upstream origin main #Ejecutar el cambio, el error arreglado
Comienzo del colaborador

cd Documentos #Abre git bash
mkdir class-git #Crea la carpeta o directorio de trabajo
ls -al #Revisa lo que va haciendo, los archivos o directorios que tiene
1. No debe hacer un git init, debe buscar el repositorio en el cual esta invitado a participar, por supuesto en GitHub.

2. Pasa a clonar desde HTTPS, copiar la url, esto es porque no se arranca el proyecto desde cero, se esta uniendo otro colaborador.

3. En git bash ponemos el siguiente comando. git clone url-copiada-github #Esto hace que clonemos el repositorio

4. No pide ni usuario ni contraseña si el repositorio es publico.

code . #Abre VSC y comienza con cambios, o abre el siguiente comando para hacer modificaciones
vim historia.txt #Vamos a escribir: Aquí esta un nuevo colaborador
vim escribimos el mensaje del commit #Esto en Ubuntu
ctrl + x
s #Para un si 
enter #Terminado el mensaje del commit
vim escribimos el mensaje del commit #Esto en git bash window
esc #Presionamos escaner luego de terminar de escribir
:wq! #Para salir del editor vim en window

git status
git commit -am "Mi primer commit, estoy muy emocionado!!!"
git pull origin main
git fetch
gti branch #Para ver las ramas que se trajo, no se trae sino solo main, si hay mas debes crearlas local
git log #Para ver toda las historia
git log --graph #Vemos el grafico de las diferentes ramas y del commit que acabamos de hacer que esta en el main, Git es una base de datos de toda las historia de todo lo que se ha hecho
git push origin main #Va a pedir un email que será el del colaborador, su contraseña.
5. Nos trae un denegado, ¿Por qué? Porque en el proceso de abordaje el jefe no le dio acceso: el dueño del repositorio no le agregó dandole acceso.

6. Ir a settings del repositorio, veremos la opsión Collaborators, agregamos el correo o nombre de usuario: el colaborador debe tener un email publico y visible o de otra manera debera ser con el nombre de usuario publico: ingresar el username y debe ir como colaborador.

7. Se puede enviar un email con la url, pero ya GitHub envia una notificación al usuario de invitado, es una cosa que debemos empezar a consultar y revisar.

8. El colaborador debe aceptar la invitación, una vez hecho eso ya tendrá total acceso para hacer push al repositorio.

git pull origin main
git push origin main #Colocar nombre de usuario y contraseña, listo
9. El dueño del repositorio no ve los cambios, ¿Qué hacer?

git pull origin main
git fetch
git log --stat #Se verá claro que el colaborador ingreso su primer commit
10. A partir de ahora el dueño del repositorio y el colaborador deberán repartir el trabajo, esto se hace con distintas ramas de trabajo: el dueño trabajará desde la rama header y el colaborador desde la rama footer, al final cuando se termine, se hara un merge para terminar el proyecto.
