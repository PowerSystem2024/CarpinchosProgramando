CLASE 06 MIÉRCOLES 18 DE SEPTIEMBRE DEL 2024 - Portafolio 6

Error con los tags Investigación: ¿Qué pasa si por error cargamos un tag dos veces?

¿Cómo solucionarías este problema o error?

La respuesta debe ser enviada antes de las 23 horas por cada grupo, deben enviar comandos y todo los pasos que harían frente a este conflicto.

Nosotros lo resolveremos aqui:

Para eliminar una etiqueta, usaremos el siguiente comando:

git tag -d "Nombre de la etiqueta"

Primero lo que deberiamos hacer seria listar los tags para ver cual tenemos duplicado ejecutamos el siguiente comando:
git tag

Eliminar el tag duplicado localmente Supongamos que el tag duplicado se llama v1.0.0. Para eliminar el tag localmente, usaremos el siguiente comando:
git tag -d v1.0.0.

Este comando solo elimina el tag en nuestro repositorio local.

Eliminar el tag duplicado en el repositorio remoto Después de eliminar el tag localmente, también debemos eliminarlo del repositorio remoto. Para hacerlo, ejecutaremos:
En el git BASH ejecutaremos

git push origin --delete v1.0.0

Este comando elimina el tag de nuestro repositorio en GitHub.

Verificación final Para asegurarnos de que todo se ha resuelto correctamente, listaremos los tags en el repositorio remoto:
git ls-remote --tags origin