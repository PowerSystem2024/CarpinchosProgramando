<script setup>
import proyecto1 from '../assets/Quiron.png';
import proyecto2 from '../assets/WebAG.png';
import proyecto3 from '../assets/WebAG2.png';
import proyecto4 from '../assets/e-commerce.png';

// Este componente muestra una galería de proyectos con información sobre cada proyecto
import { ref } from 'vue';
//.ref es una función que se utiliza para crear una referencia reactiva en Vue 3
var misProyectos = ref([]);
//.value es una propiedad que se utiliza para acceder al valor de una referencia reactiva en Vue 3
misProyectos.value = ([
    //esto es un array de objetos que contiene información sobre los proyectos
    {
        id: 1,
        src: proyecto1,
        titulo: "Aplicación Movil para Quiron Gym.",
        descripcion: "Creé una aplicación móvil de gestion para un gimnasio donde los usuarios y el administrador pueden crear perfiles y manejar horarios y pagos. Inclui APIs y bases de datos",
    },
    {
        id: 2,
        src: proyecto2,
        titulo: "Plataforma Web - Profesora de español.",
        descripcion: "Diseñé y desarrollé una pagina web para una profesora de español para extranjeros. El desarrollo lo implementé usando herramientas como HTML, CSS y Javascript."
    },
    {
        id: 3,
        src: proyecto3,
        titulo: "Pagina Web para aprendizaje de español especial para extranjeros.",
        descripcion: "Diseñé y desarrollé una pagina web para aprendizaje de español para extranjeros. El desarrollo lo implementé usando herramientas como HTML, CSS y Javascript."
    },
    {
        id: 4,
        src: proyecto4,
        titulo: "E-commerce Relojería",
        descripcion: "Participé en un grupo de diseño y desarrollo de un E-commerce para una relojería. Implementamos APIs y distintas tecnologias y lenguajes de programación"
    },
])
</script>

<template>
    <!-- Aquí va el código HTML de la galería de proyectos -->
    <div class="galeria">
        <!-- Itera sobre cada proyecto en la lista de misProyectos -->
        <!--key es una propiedad especial que se utiliza para identificar de forma única cada elemento en una lista de Vue.js-->
        <ul>
            <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
                <!-- Muestra la imagen del proyecto utilizando : que es una directiva de enlace de atributo en Vue.js -->
                <img :src="proyecto.src" :alt="proyecto.titlulo">
                <div class="proyecto-info">
                    <!-- Muestra el título y la descripción del proyecto utilizando la interpolación de Vue.js -->
                    <h3>{{ proyecto.titulo }}</h3>
                    <p>{{ proyecto.descripcion }}</p>
                </div>
            </li>
        </ul>
    </div>
</template>

<style scoped>
/* Estilos Fondo Animado de Css de la galería */
/* La clase 'galeria' es el contenedor principal de la galería de proyectos */
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
    background: linear-gradient(-45deg, #021526, #03346E, #6EACDA, #E2E2B6);
    /* Ajusta el tamaño del fondo para que cubra el área completa */
    background-size: 400% 400%;
    /* Aplica una animación al fondo que dura 15 segundos, tiene una transición suave y se repite infinitamente */
    animation: gradient 15s ease infinite;
    border-radius: 20px;
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
    border: 2px solid #ddd;
    /* Redondea las esquinas del contenedor */
    border-radius: 8px;
    /* Oculta cualquier contenido que se desborde del contenedor */
    overflow: hidden;
    /* Establece un color de fondo claro para el proyecto */
    background-color: #d0d0d0;
    /* Define el ancho máximo del proyecto en 222px */
    max-width: 900px;
    /* Hace que el contenedor se ajuste flexiblemente ocupando al menos 300px de ancho */
    flex: 1 1 auto;
    margin-bottom: 1rem;
}

/* Estilo para las imágenes dentro del contenedor 'proyecto' */
.proyecto img {
    /* Establece un tamaño fijo para las imágenes */
    width: 550px; /* Cambia este valor según lo que necesites */
    height: 300px; /* Cambia este valor según lo que necesites */
    /* Mantiene la relación de aspecto */
    object-fit: cover; /* Esto recorta la imagen si es necesario para ajustarse al tamaño */
    display: block;
    margin: 0 auto; /* Centra la imagen horizontalmente */
    border-radius: 15px;
    padding: 0.5rem;
}

/* La clase 'proyecto-info' contiene la información del proyecto */
.proyecto-info {
    /* Agrega un padding de 15px alrededor de la información */
    padding: 15px;
    /* Centra el texto dentro del contenedor */
    text-align: center;
}

.proyecto-info h3 {
    margin: 10px 0;
    font-size: 26px;
    color: #000000;
    font-weight: bolder;
    line-height: 1.2;
    text-shadow: #3c3c3b;
}

/* Estilo para los párrafos de los proyectos */
.proyecto-info p {
    /* Establece un margen superior e inferior de 10px */
    margin: 10px 0;
    /* Define el tamaño de la fuente a 1em (igual al tamaño de fuente base) */
    font-size: 20px;
    /* Aplica un color gris (#666) al texto */
    color: #191919;
}

</style>
