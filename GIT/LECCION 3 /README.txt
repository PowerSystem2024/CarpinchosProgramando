CLASE 03 MIÉRCOLES 28 DE AGOSTO DEL 2024 - Portafolio 3

Cambios en GitHub: de master a main
El escritor Argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso. Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.

Sí, esta lectura es parte de la enseñanza profesional de Git & GitHub.

Desde el 1 de octubre de 2020 GitHub cambió el nombre de la rama principal: ya no es “master” -como aprenderás aquí- sino main.

Este derivado de una profunda reflexión ocasionada por el movimiento #BlackLivesMatter.

La industria de la tecnología lleva muchos años usando términos como master, slave, blacklist o whitelist y esperamos pronto puedan ir desapareciendo.

Y sí, las palabras importan.

Por lo que de aquí en adelante cada vez que me escuches mencionar “master” debes saber que hago referencia a “main”.

¿Cuando es que sigue siendo "master" y cuando sigue siendo "main"?

Cuando se crea un repositorio desde git bash en nuestro ordenador a través de git init, sigue siendo el estandar como master. ¿Qué hacer con esto? Debes cambiar el nombre de la rama master a main con el comando "git branch -M main". Ahora cuando creamos un repositorio desde la nube, osea desde GitHub, ya verás que la rama principal tiene por default el nombre de "main" y al clonar a nuestro ordenador seguira teniendo este nombre y no será necesario ningun cambio.