![image](https://github.com/user-attachments/assets/191083e9-5cc4-470b-8217-096a8d8d4618)

# **Clase 1**

**COMANDOS**

***Import repository, New repository, New organization:** significa que es como tu empresa*

***New project:** significa es como un grupo de repositorios que puedes tener dentro de una empresa. *

***New gist:** es un pedacito de código que puedes compartir*

**New repository Ponemos el nombre:** class-git.

**Create repository:** Lo ponemos en privado o en Publico.

El **README.md** es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.

Para **clonar** un repositorio desde GitHub (o cualquier otro servidor remoto) debemos **copiar la URL** (por ahora, usando HTTPS) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

![capturaGit1](https://github.com/user-attachments/assets/f781b837-8465-4e1c-9d8b-45eb95334dfe)

ATENCIÓN: ¿Por qué? **Porque a través de https nos pedirá usuario(nombre perfil) y contraseña.**

Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.

Cómo conectar un repositorio de GitHub a nuestro documento local: Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:

* [ ]  **Guardar la URL del repositorio de GitHub con el nombre de origin**
* [ ]  **git remote add origin URL**

**Verificar que la URL se haya guardado correctamente:**

* [ ]  **git remote**
* [ ]  **git remote -v**

![capturaGit2](https://github.com/user-attachments/assets/374bfd26-94f0-4bf0-88b0-4ecb3192d74e)

Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. Podemos usar **git fetch y git merge** o solo **git pull con el flag --allow-unrelated-histories:**

**git pull origin master --allow-unrelated-histories**

![capturaGit3](https://github.com/user-attachments/assets/45fb38fa-0111-450b-a15f-922d260f7b15)

Por último, ahora sí podemos hacer git push para guardar los cambios de nuestro repositorio local en GitHub:

**git push origin master**

### **Cómo autenticarte en GitHub 2022**

Antes de empezar debemos renombrar la rama **‘máster’ a ‘main’,** este es el nuevo estándar en GitHub, para esto:

Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.

Ejecutamos el siguiente comando: **git branch -M main**

![capturaGit4](https://github.com/user-attachments/assets/0502c165-99fd-4edd-9f14-a461a3eea914)

![capturaGit5](https://github.com/user-attachments/assets/1cce9a6f-7df6-4f19-9ffa-ad48f1117f25)

![capturaGit6](https://github.com/user-attachments/assets/4388b7dd-7734-48c8-82cd-918f24bc29fb)

#### Pasos para crear un token de acceso personal.

Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.

#### **Descubre el uso de tags en Github**

Seguir la secuencia: **Ingresamos a nuestra cuenta de GitHub.**

**Buscamos Settings**

**Click en Developer settings**

**Click en Personal access tokens**

**Click en Generate new token aquí se puede colocar un nombre, la fecha de expiración.**

**Tildar en repo y luego click en el botón verde Generate token**

![capturaGit7](https://github.com/user-attachments/assets/4389be4c-fe74-4dea-9a7a-9e192f2f991e)

# Clase 2

**Vamos a cargar la llave SSH publica en GitHub**

![capturaGit8](https://github.com/user-attachments/assets/c887c63b-9516-4ef8-adfe-62fd538d87d0)

**Para copiar la llave publica debes ir al archivo .ssh y allí encontrarás el archivo .pub lo podes abrir con el txt, luego copiar el contenido que esta dentro.**

![capturaGit9](https://github.com/user-attachments/assets/73fcfa2c-94e2-4846-9c58-e48d9889c374)

**copiar la llave publica #Ir a GitHub, vamos a setting, vamos a SSH and GPG keys**

**crear una nueva #New SSH key poner nombre y pegar la ssh publica, con esto esta listo.**

![capturaGit10](https://github.com/user-attachments/assets/65774b10-49a5-4fc0-b49c-f1bc9d9b9f0e)

**Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.**

**git branch #Vemos en que rama estamos**

**git checkout master #Ponernos en la rama master**

**git branch -M main #Cambiamos el nombre a la rama master**

**git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo**

**git remote -v #Vemos si ya esta conectado**

**git merge segunda #Mergeamos lo que tenemos en la rama segunda en main**

**git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy**

**git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.**

![capturaGit11](https://github.com/user-attachments/assets/78215343-3687-48c4-8f7b-270d9c5f886d)

![capturaGit12](https://github.com/user-attachments/assets/207c2a1b-affb-4d02-9858-931f449a8de8)

**Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.**

# **Clase 3**

Cambios en GitHub: de master a main

El escritor Argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso.

Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.

Sí, esta lectura es parte de la enseñanza profesional de Git & GitHub.

Desde el 1 de octubre de 2020 GitHub cambió el nombre de la rama principal: ya no es “master” -como aprenderás aquí- sino main.

Este derivado de una profunda reflexión ocasionada por el movimiento #BlackLivesMatter.

La industria de la tecnología lleva muchos años usando términos como master, slave, blacklist o whitelist y esperamos pronto puedan ir desapareciendo.

Y sí, las palabras importan.

Por lo que de aquí en adelante cada vez que me escuches mencionar “master” debes saber que hago referencia a “main”.

¿Cuando es que sigue siendo master y cuando sigue siendo main?

![capturaGit13](https://github.com/user-attachments/assets/56d41b37-368a-4a97-9922-3c80c5a73441)

Cuando se crea un repositorio desde git bash en nuestro ordenador a través de git init, sigue siendo el estandar como master. ¿Qué hacer con esto? Debes cambiar el nombre de la rama master a main con el comando git branch -M main.

![capturaGit14](https://github.com/user-attachments/assets/bf370d01-e734-4acb-8a12-88822b328a0f)

Ahora cuando creamos un repositorio desde la nube, osea desde GitHub, ya verás que la rama principal tiene por default el nombre de main y al clonar a nuestro ordenador seguira teniendo este nombre y no será necesario ningun cambio.

# **Clase 4**

**Tu primer push**

**La creación de las SSH es necesario solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.**

![CapturaGit15](https://github.com/user-attachments/assets/e8bd1090-6a30-4580-b8d8-0016a303c8dd)

**Luego de crear nuestras llaves SSH podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.**

![CapturaGit16](https://github.com/user-attachments/assets/95a5d623-84ea-4e96-b9e0-6d1177fae954)

**Para esto debes entrar a la Configuración de Llaves SSH en GitHub, crear una nueva llave con el nombre que le quieras dar y el contenido de la llave pública de tu computadora.**

**Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:**

### ssh

**git remote set-url origin url-ssh-del-repositorio-en-github**

**Comandos para copiar la llave SSH:**

![CapturaGit17](https://github.com/user-attachments/assets/14ad7bc4-441d-415f-9721-77a0660ce345)

**ESTAS SON LAS RUTAS DEL SSH PUBLICO**

Mac:
pbcopy < ~/.ssh/id_rsa.pub

### Windows (Git Bash):

### clip < ~/.ssh/id_rsa.pub

Linux (Ubuntu):
cat ~/.ssh/id_rsa.pub

![CapturaGit18](https://github.com/user-attachments/assets/365d1ea2-e5cc-4b23-aa9f-9a56f753b852)

![CapturaGit19](https://github.com/user-attachments/assets/e1ab81ee-0b33-4aff-99ce-a591297cf6c4)

## Importante

**Las buenas costumbres nos enseñan que antes de hacer un push, siempre debemos hacer un pull, un fetch, esto para que si alguien ya hizo algún cambio, no se genere un conflicto.**

### Invitar a un colaborador

**Para invitar a un colaborador debemos ir a GitHub y seleccionar:**
**setting -> colaborators -> ingresar contraseña o un F2A de verificación y enviar la invitación escribiendo el nombre de usuario.**

![CapturaGit20](https://github.com/user-attachments/assets/f3c8f7fc-9a6a-4f64-aa0f-4e9d2fa816d3)

![CapturaGit21](https://github.com/user-attachments/assets/5f0c927b-6d61-446b-a991-8496057d9d8e)

**Del otro lado el usuario invitado solo debe aceptar y listo, ya puede participar del proyecto haciendo commit.**

# **Clase 5**

**Git tag y versiones en GitHub**

**En Git, las etiquetas o Git tags tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando git tag, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.**

**Creación de etiquetas en Git**

```sh
git tag

```

**Sustituye con un identificador semántico que refleje el estado del repositorio en el momento de la creación. Git admite etiquetas anotadas y ligeras.**

**Listado de etiquetas**
**Para obtener una lista de etiquetas en el repositorio, ejecuta el siguiente comando:**

**Para crear una etiqueta, ejecuta el siguiente comando:**

**Las etiquetas anotadas almacenan información adicional como la fecha, etiquetador y correo electrónico, y son ideales para publicaciones públicas. Las etiquetas ligeras son más simples y se emplean como “marcadores” de una confirmación específica.**

### **git tag**

**Esto mostrará una lista de las etiquetas existentes, como:**

### **v1.0**

### **v1.1**

### **v1.2**

![CapturaGit22](https://github.com/user-attachments/assets/498d6190-0d7d-4d7e-b1ac-f92e92dd8be9)

**Para perfeccionar la lista, puedes utilizar opciones adicionales, como -l con una expresión comodín.**

**Uso compartido de etiquetas**

**Compartir etiquetas requiere un enfoque explícito al usar el comando git push. Por defecto, las etiquetas no se envían automáticamente. Para enviar etiquetas específicas, utiliza:**

**git push origin**

**Para enviar varias etiquetas a la vez, usa:**

**git push origin --tags**

![CapturaGit23](https://github.com/user-attachments/assets/9139f697-2420-4ef4-8ed4-3bf12b689ae2)

**Eliminación de etiquetas**
**Para eliminar una etiqueta, usa el siguiente comando:**

### **git tag -d***

**Esto eliminará la etiqueta identificada por en el repositorio local.**

![CapturaGit24](https://github.com/user-attachments/assets/169b4110-4a1d-4078-b3a9-9e1481a73079)

**En resumen, las etiquetas en Git son esenciales para asignar versiones y capturar instantáneas importantes en el historial de un proyecto. Aprender a crear, listar, compartir y eliminar etiquetas mejorará tu flujo de trabajo con Git.**

# **Clase 6**

### **Error con los tags**

### Investigación: ¿Qué pasa si por error cargamos un tag dos veces?

### ¿Cómo solucionarías este problema o error?

### DESARROLLO:

### En Git, un tag es una referencia a un commit específico y se utiliza comúnmente para marcar versiones de un proyecto.

- ### Problema: Si intentamos crear un tag con el mismo nombre que uno existente, Git mostrrá un error. Los tags en Git deben ser únicos dentro de un repositorio.

## Ejemplo

1. Crea un tag:

   ```bash
    git tag v1.0
   ```

### Intentar crear el mismo tag nuevamente provocará un error

git tag v1.0
### Esto producirá un error: "fatal: tag 'v1.0' already exists".

![CapturaGit25](https://github.com/user-attachments/assets/6f3d11f0-d413-48fb-8dfe-a6b4fd9caa18)

### Si necesitas cambiar el tag (por ejemplo, apuntarlo a un commit diferente), deberás eliminar el tag existente primero, ya que no puedes sobrescribirlo directamente.

      ```bash
      git tag -d v1.0  # Elimina el tag
      git tag v1.0 -m "nuevoCommit"

### Crea un nuevo tag apuntando a un commit diferente

![CapturaGit26](https://github.com/user-attachments/assets/15e39b4f-7c22-47f3-9d9f-db6b404e8e3e)

### Considera usar tags anotados en lugar de tags ligeros. Los tags anotados incluyen más información (como el autor y la fecha) y son más fáciles de manejar:

      ```bash
        git tag -a v1.0 -m "Versión 1.0"  # Crea un tag anotado
![CapturaGit27](https://github.com/user-attachments/assets/e15d842b-a3f7-4438-8081-7c30a9d343c6)

### Para ver la información de un tag anotado en Git, puedes usar el siguiente comando:

      ```bash
        git show Version4.0
### Tambien se pueden ver los detalles de los tags con este comando:

### Ver detalles de todos los tags:

      ```bash
        git show-ref --tags
![CapturaGit28](https://github.com/user-attachments/assets/747a8e40-6018-425f-80dc-5c6259610ab0)

# **Clase 7**

**Error con los tags**
**Investigación: Si un tag es imposible generarlo dos veces ¿Cómo es que existe el error de dos tags con el mismo nombre?**

![CapturaGit30](https://github.com/user-attachments/assets/9d7d9501-b699-42e5-8bdc-2668b7e6b9f3)

**¿Cómo se origina este problema o error?**

![CapturaGit29](https://github.com/user-attachments/assets/227dabe3-22d4-4ec4-8325-f164bf3824c7)

# **Clase 8**

***Manejo de Ramas en Github***

***Si no te funciona el comando gitk es posible no lo tengas instalado por defecto.***
***Para instalar gitk debemos ejecutar los siguientes comandos:***

```sh
sudo apt-get update
sudo apt-get install gitk
```
## Repasa: ¿Qué es Git?

##### Las ramas nos permiten hacer cambios a nuestros archivos sin modificar la versión principal (main). Puedes trabajar con ramas que nunca envías a GitHub, así como pueden haber ramas importantes en GitHub que nunca uses en el repositorio local. Lo crucial es que **aprendas a manejarlas** para trabajar profesionalmente.

##### Si, estando en otra rama, modificamos los archivos y hacemos `commit`, tanto el historial (`git log`) como los archivos serán afectados. La ventaja que tiene usar ramas es que las modificaciones solo afectarán a esa rama en particular. Si luego de “guardar” los archivos (usando `commit`) nos movemos a otra rama (`git checkout otraRama`), veremos cómo las modificaciones de la rama pasada no aparecen en la otraRama.

### Comandos para manejo de ramas en GitHub

**Crear una rama:**

sh
Copiar código
git branch branchName        # Crear una rama
git checkout branchName      # Movernos a otra rama
git checkout -b nombre-de-la-rama  # Crear una rama en el repositorio local
git push origin nombre-de-la-rama   # Publicar una rama local al repositorio remoto

![CapturaGit31](https://github.com/user-attachments/assets/b349499e-f676-4a98-88e0-e69bdfeedd1b)

Recuerda que podemos ver gráficamente nuestro entorno y flujo de trabajo local con Git utilizando el comando gitk. Gitk fue el primer visor gráfico que se desarrolló para ver de manera gráfica el historial de un repositorio de Git.

![CapturaGit32](https://github.com/user-attachments/assets/74ef692d-dcee-4479-b859-31ddd66ad2e2)

# **Clase 9**

Configurar múltiples colaboradores en un repositorio de GitHub

Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits, ni ramas. Esto quiere decir que pueden copiar tu proyecto pero no colaborar con él, si este es publico, de otra manera, osea, si es privado es necesario que realmente estes haciendo una invitación, sino no lo van a poder ver. Existen varias formas de solucionar esto para poder aceptar contribuciones. Una de ellas es añadir a cada persona de nuestro equipo como colaborador de nuestro repositorio.**

**Cómo agregar colaboradores en Github**
**Solo debemos entrar a la configuración de colaboradores de nuestro proyecto. Se encuentra en:**

**Repositorio > Settings > Collaborators
Ahí, debemos añadir el email o username de los nuevos colaboradores.**

![1728673386167](images/SegundoSemestre/1728673386167.png)

**Si como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar de la siguiente manera:**

**Hacer un commit con el nuevo mensaje que queremos, esto nos abre el editor de texto de la terminal:**

**git commit —amend  # Corregimos el mensaje

git pull origin main # Traer el repositorio remoto

git push --set-upstream origin main  # Ejecutar el cambio, el error arreglado

Comienzo del colaborador

cd Documentos  # Abre git bash

mkdir class-git  # Crea la carpeta o directorio de trabajo

ls -al  # Revisa lo que va haciendo, los archivos o directorios que tiene

##### 1. No debe hacer un git init, debe buscar el repositorio en el cual esta invitado a participar, por supuesto en GitHub.

##### 2. Pasa a clonar desde HTTPS, copiar la url, esto es porque no se arranca el proyecto desde cero, se esta uniendo otro colaborador.

##### 3. En git bash ponemos el siguiente comando.

git clone url-copiada-github #Esto hace que clonemos el repositorio

##### 4. No pide ni usuario ni contraseña si el repositorio es publico.

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

##### 5. Nos trae un denegado, ¿Por qué? Porque en el proceso de abordaje el jefe no le dio acceso: el dueño del repositorio no le agregó dandole acceso.

##### 6. Ir a settings del repositorio, veremos la opción Collaborators, agregamos el correo o nombre de usuario: el colaborador debe tener un email publico y visible o de otra manera debera ser con el nombre de usuario publico: ingresar el username y debe ir como colaborador.

##### 7. Se puede enviar un email con la url, pero ya GitHub envia una notificación al usuario de invitado, es una cosa que debemos empezar a consultar y revisar.

##### 8. El colaborador debe aceptar la invitación, una vez hecho eso ya tendrá total acceso para hacer push al repositorio.

git pull origin main

git push origin main #Colocar nombre de usuario y contraseña, listo

##### 9. El dueño del repositorio no ve los cambios, ¿Qué hacer?

git pull origin main

git fetch

git log --stat #Se verá claro que el colaborador ingreso su primer commit

##### 10. A partir de ahora el dueño del repositorio y el colaborador deberán repartir el trabajo, esto se hace con distintas ramas de trabajo: el dueño trabajará desde la rama header y el colaborador desde la rama footer, al final cuando se termine, se hara un merge para terminar el proyecto.

# **Clase 10**

Flujo de trabajo profesional

Haciendo merge de ramas de desarrollo a main

Para poder desarrollar software de manera óptima y ordenada, necesitamos tener un flujo de trabajo profesional, que nos permita trabajar en conjunto sin interrumpir el trabajo de otros desarrolladores.

Una buena práctica de flujo de trabajo sería la siguiente:

Crear ramas
Asignar una rama a cada programador
El programador baja el repositorio con git pull origin master
El programador cambia de rama
El programador trabaja en esa rama y hace commits
El programador sube su trabajo con git push origin #nombre_rama
El encargado de organizar el proyecto baja, revisa y unifica todos los cambios