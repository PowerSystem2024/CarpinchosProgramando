CLASE 05 MIÉRCOLES 11 DE SEPTIEMBRE DEL 2024 - Portafolio 5

Git tag y versiones en GitHub

En Git, las etiquetas o Git tags tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando git tag, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.

Creación de etiquetas en Git git tag

Sustituye con un identificador semántico que refleje el estado del repositorio en el momento de la creación. Git admite etiquetas anotadas y ligeras.

Listado de etiquetas Para obtener una lista de etiquetas en el repositorio, ejecuta el siguiente comando:

$ git tag -a v1.0 -m "Product release" git tag -a ronburgundy -m "Brick killed a guy a trident."

Para crear una etiqueta, ejecuta el siguiente comando:

Las etiquetas anotadas almacenan información adicional como la fecha, etiquetador y correo electrónico, y son ideales para publicaciones públicas. Las etiquetas ligeras son más simples y se emplean como “marcadores” de una confirmación específica.

git tag

Esto mostrará una lista de las etiquetas existentes, como:

v1.0

v1.1

v1.2

Para perfeccionar la lista, puedes utilizar opciones adicionales, como -l con una expresión comodín.

Uso compartido de etiquetas

Compartir etiquetas requiere un enfoque explícito al usar el comando git push. Por defecto, las etiquetas no se envían automáticamente. Para enviar etiquetas específicas, utiliza:

git push origin

Para enviar varias etiquetas a la vez, usa:

git push origin --tags

Eliminación de etiquetas Para eliminar una etiqueta, usa el siguiente comando:

git tag -d

Esto eliminará la etiqueta identificada por en el repositorio local.

En resumen, las etiquetas en Git son esenciales para asignar versiones y capturar instantáneas importantes en el historial de un proyecto. Aprender a crear, listar, compartir y eliminar etiquetas mejorará tu flujo de trabajo con Git.