<script setup>

</script>

<template>
    <div class="galeria">
        <div class="proyecto">
            <img src="/src/assets/Proyectos/proyecto1.jpg" alt="Proyecto 1">
            <div class="proyectoInfo">
                <h3>Yo Dibujo</h3>
                <p>Creé una página web en un curso de programación web (Yo Puedo Programar - Junior Achievement) con los lenguajes HTML, CSS y JavaScript.</p>
                <div class="proyectoLinks">
                    <a href="" class="btnVerMas" target="_blank" rel="noopener noreferrer">Ver Proyecto</a>
                    <a href="https://github.com/anaprg05/YoDibujo.git" class="githubLink" target="_blank" rel="noopener noreferrer">Ver Código en GitHub</a>
                </div>
            </div>
        </div>
        
        <div class="proyecto">
            <img src="/src/assets/Proyectos/proyecto2.jpg" alt="Proyecto 2">
            <div class="proyectoInfo">
                <h3>PCB en Electrónica</h3>
                <p>Creé una página web para una equivalencia del Instituto Leonardo Murialdo con los lenguajes HTML, CSS y JavaScript.</p>
                <div class="proyectoLinks">
                    <a href="" class="btnVerMas" target="_blank" rel="noopener noreferrer">Ver Proyecto</a>
                    <a href="https://github.com/anaprg05/EquivalenciasElectro.git" class="githubLink" target="_blank" rel="noopener noreferrer">Ver Código en GitHub</a>
                </div>
            </div>
        </div>

        <div class="proyecto">
            <img src="/src/assets/Proyectos/proyecto3.jpg" alt="Proyecto 3">
            <div class="proyectoInfo">
                <h3>Beneficios de la Robótica y la Electrónica</h3>
                <p>Creé una página web para una equivalencia del Instituto Leonardo Murialdo con los lenguajes HTML, CSS y JavaScript.</p>
                <div class="proyectoLinks">
                    <a href="" class="btnVerMas" target="_blank" rel="noopener noreferrer">Ver Proyecto</a>
                    <a href="https://github.com/anaprg05/EquivalenciasElectro.git" class="githubLink" target="_blank" rel="noopener noreferrer">Ver Código en GitHub</a>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.galeria {
    /* Establece el ancho de la galería al 100% del contenedor padre */
    width: 100%;
    /* Establece la altura de la galería al 100% del contenedor padre */
    height: 100%;
    /* Utiliza flexbox para organizar los elementos hijos en la galería */
    display: flex;
    /* Permite que los elementos se ajusten y pasen a la siguiente línea si no caben en una sola fila */
    flex-wrap: wrap;
    /* Establece un espacio de 20px entre los elementos de la galería */
    gap: 20px;
    /* Agrega un padding de 20px alrededor de la galería */
    padding: 20px;
    /* Centra los elementos hijos horizontalmente */
    justify-content: center;
    /* Aplica un fondo con un degradado de colores */
    background: linear-gradient(-45deg, #DDE5B6, #B9CA88, #9B8965, #6C584C);
    /* Ajusta el tamaño del fondo para que cubra el área completa */
    background-size: 400% 400%;
    /* Aplica una animación al fondo que dura 15 segundos, tiene una transición suave y se repite infinitamente */
    animation: gradient 15s ease infinite;
    border-radius: 5px;
}

/* Define una animación llamada 'gradient' para cambiar la posición del fondo */
@keyframes gradient {

/* Al inicio, el fondo está posicionado en el 0% horizontal y 50% vertical */
0% {
    background-position: 0% 50%;
}

/* A la mitad de la animación, el fondo se desplaza al 100% horizontal y 50% vertical */
50% {
    background-position: 100% 50%;
}

/* Al final, el fondo vuelve a la posición inicial */
100% {
    background-position: 0% 50%;
}
}

/* La clase 'proyecto' es el contenedor individual de cada proyecto */
.proyecto {
/* Utiliza flexbox para organizar el contenido del proyecto en una columna */
display: flex;
/* Establece la dirección de los elementos en columna */
flex-direction: column;
/* Aplica un borde de 2px sólido y color gris claro (#ddd) alrededor del proyecto */
border: 2px solid #C5D397;
/* Redondea las esquinas del contenedor */
border-radius: 8px;
/* Oculta cualquier contenido que se desborde del contenedor */
overflow: hidden;
/* Establece un color de fondo claro para el proyecto */
background-color: #ADC178;
/* Define el ancho máximo del proyecto en 222px */
max-width: 222px;
/* Hace que el contenedor se ajuste flexiblemente ocupando al menos 300px de ancho */
flex: 1 1 300px;
}

/* Estilo para las imágenes dentro del contenedor 'proyecto' */
.proyecto img {
/* Hace que la imagen ocupe el 100% del ancho del contenedor */
width: 100%;
/* Mantiene la relación de aspecto de la imagen */
height: auto;
/* Asegura que la imagen se muestre como un bloque, sin espacio en línea alrededor */
display: block;
}

/* La clase 'proyecto-info' contiene la información del proyecto */
.proyectoInfo {
/* Agrega un padding de 15px alrededor de la información */
padding: 15px;
/* Centra el texto dentro del contenedor */
text-align: center;
}

/* Estilo para los títulos de los proyectos */
.proyectoInfo h3 {
/* Establece un margen superior e inferior de 10px */
margin: 10px 0;
/* Define el tamaño de la fuente a 1.3em (relativo al tamaño de fuente del contenedor) */
font-size: 1.3em;
/* Aplica un color gris oscuro (#333) al texto */
color: #5e4c41;
}

/* Estilo para los párrafos de los proyectos */
.proyectoInfo p {
/* Establece un margen superior e inferior de 10px */
margin: 10px 0;
/* Define el tamaño de la fuente a 1em (igual al tamaño de fuente base) */
font-size: 1em;
/* Aplica un color gris (#666) al texto */
color: #755948;
}

/* La clase 'proyecto-links' organiza los enlaces y botones del proyecto */
.proyectoLinks {
/* Utiliza flexbox para organizar los enlaces en una columna */
display: flex;
/* Establece la dirección de los elementos en columna */
flex-direction: column;
/* Establece un espacio de 10px entre los elementos */
gap: 10px;
/* Agrega un margen superior de 10px */
margin-top: 10px;
}

/* Estilo para el botón 'Ver Más' dentro de la clase 'proyecto-links' */
.proyectoLinks .btnVerMas {
/* Aplica un color de fondo azul (#007BFF) */
background-color: #c3d87d;
/* Aplica un color de texto blanco */
color: #8f6246;
/* Agrega un padding de 10px en vertical y 15px en horizontal */
padding: 10px 15px;
/* Redondea las esquinas del botón */
border-radius: 5px;
/* Elimina el subrayado del texto */
text-decoration: none;
/* Aplica una transición suave al cambiar el color de fondo */
transition: background-color 0.3s;
}

/* Estilo para cuando el botón 'Ver Más' es hover */
.proyectoLinks .btnVerMas:hover {
/* Cambia el color de fondo a un azul más oscuro (#0056b3) */
background-color: #91a164;
}

/* Estilo para el enlace a GitHub dentro de la clase 'proyecto-links' */
.proyectoLinks .githubLink {
/* Aplica un color gris oscuro (#333) al texto */
color: #8f6246;
/* Elimina el subrayado del texto */
text-decoration: none;
/* Establece el tamaño de fuente a 0.9em (un poco más pequeño que el tamaño base) */
font-size: 0.9em;
}

/* Estilo para cuando el enlace a GitHub es hover */
.proyectoLinks .githubLink:hover {
/* Añade un subrayado al texto */
text-decoration: underline;
}
</style>
