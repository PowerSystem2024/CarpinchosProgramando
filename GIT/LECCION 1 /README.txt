CLASE 01 MIÉRCOLES 14 DE AGOSTO DEL 2024 - Portafolio 1

USO DE GITHUB Parte 1

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.

---------------------------------------------------------------------------------------------
COMANDOS
Import repository, New repository, New organization: #significa que es como tu empresa, New project: significa es como un grupo de repositorios que puedes tener dentro de una empresa, New gist: es un pedasito de código que puedes compartir

New repository #Ponemos el nombre: class-git, descripción: Haremos un blog increible, hay muchas licencias para publicar el código: NO lo hacemos ahora.

Create repository #Lo ponemos en privado o en Publico.

--------------------------------------------------------------------------------------------

El README.md es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.

Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando HTTPS) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

----------------------------------------------------------------------------------------------------
Cómo conectar un repositorio de GitHub a nuestro documento local Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:
## Guardar la URL del repositorio de GitHub con el nombre de origin

$ git remote add origin URL

## Verificar que la URL se haya guardado correctamente:

$ git remote

$ git remote -v

## Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. 

#Podemos usar git fetch y git merge o solo git pull con el flag 

$ git pull --allow-unrelated-histories:

$ git pull origin master --allow-unrelated-histories

# Por último, ahora sí podemos hacer git push para guardar los cambios de nuestro repositorio local en GitHub:

$ git push origin master
------------------------------------------------------------------------------------------------------

Cómo autenticarte en GitHub 2022

Antes de empezar debemos renombrar la rama ‘máster’ a ‘main’, este es el nuevo estándar en GitHub, para esto:

Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.

Ejecutamos el siguiente comando: $ git branch -M main

Pasos para crear un token de acceso personal.

Inicia sesión en GitHub:

Ve a GitHub e inicia sesión con tu cuenta. Accede a la configuración de tu cuenta: Haz clic en tu avatar en la esquina superior derecha de la página y selecciona "Settings" (Configuración).

Ve a la sección de desarrolladores:

En el menú de la izquierda, desplázate hacia abajo y selecciona "Developer settings" (Configuración de desarrollador).

Crea un nuevo token:

En la sección de "Personal access tokens", selecciona "Tokens classic" y luego haz clic en "Generate new token" (Generar nuevo token).

Configura el token:

Asigna un nombre descriptivo al token para recordar su propósito. Selecciona la duración del token (por ejemplo, 30 días, 60 días, etc.) o déjalo sin fecha de expiración. Selecciona los permisos necesarios para el token, dependiendo de lo que necesites hacer (repositorios, notificaciones, paquetes, etc.).

Genera y guarda el token:

Haz clic en "Generate token" (Generar token). Importante: Copia y guarda el token en un lugar seguro, ya que no podrás verlo nuevamente una vez que cierres esta ventana.

Usa el token:

Puedes utilizar este token en lugar de tu contraseña al autenticarte en GitHub desde la línea de comandos o herramientas que requieran acceso a tu cuenta de GitHub.

Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.

Descubre el uso de tags en Github

Ver los Tags en GitHub:

Navega a tu repositorio en GitHub.
Ve a la pestaña "Tags" en la sección de "Releases" para ver todos los tags.
Crear una release desde un Tag:

En la pestaña "Releases", haz clic en "Draft a new release".
Selecciona el tag que deseas asociar con la release.
Llena los detalles como título, descripción y, si es necesario, adjunta binarios o archivos para la release.
Haz clic en "Publish release" para crear una nueva release basada en el tag seleccionado.
