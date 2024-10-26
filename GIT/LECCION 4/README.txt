CLASE 04 MIÉRCOLES 4 DE SEPTIEMBRE DEL 2024 - Portafolio 4

Tu primer push La creación de las SSH es necesario solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.
Luego de crear nuestras llaves SSH podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.

Para esto debes entrar a la Configuración de Llaves SSH en GitHub, crear una nueva llave con el nombre que le quieras dar y el contenido de la llave pública de tu computadora.

Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:

ssh

git remote set-url origin url-ssh-del-repositorio-en-github

Comandos para copiar la llave SSH:

ESTAS SON LAS RUTAS DEL SSH PUBLICO -Mac: pbcopy < ~/.ssh/id_rsa.pub

Windows (Git Bash):

clip < ~/.ssh/id_rsa.pub

Linux (Ubuntu):

cat ~/.ssh/id_rsa.pub

Importante

Las buenas costumbres nos enseñan que antes de hacer un push, siempre debemos hacer un pull, un fetch, esto para que si alguien ya hizo algún cambio, no se genere un conflicto.

Invitar a un colaborador

Para invitar a un colaborador debemos ir a GitHub y seleccionar: setting -> colaborators -> ingresar contraseña o un F2A de verificación y enviar la invitación escribiendo el nombre de usuario.

Del otro lado el usuario invitado solo debe aceptar y listo, ya puede participar del proyecto haciendo commit.