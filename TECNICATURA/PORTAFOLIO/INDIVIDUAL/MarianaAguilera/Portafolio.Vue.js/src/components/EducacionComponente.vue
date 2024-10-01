
<script setup>
import { ref } from 'vue';
const fechaColor = ref([]);
fechaColor.value = [
    {color: '#41516c'},
    {color: '#FBCA3E'},
    {color: '#E24A68'},
    {color: '#185F8C'},
    {color: '#4CADAD'}
];
const educacion = ref([]);
educacion.value = [
    {fecha: '2024', title: 'Tecnicatura Universitaria en Programación', descripcion: 'Incumbencias Profesionales: Operación y programación de computadoras, desarrollo de programas en distintos lenguajes, análisis y control de sistemas informáticos.', enlace: 'https://www.youtube.com/'},
    {fecha: '2024', title: 'Curso de Introducción a Python', descripcion: 'Aprendizaje práctico y contenido teórico', enlace: 'https://tourmaline-bean-2ae.notion.site/Introducci-n-a-Python-2-2024-41ba918d36cb43259ae6c21ce26c768b'},
    {fecha: '2023', title: 'Curso HTML y CSS (en curso)', descripcion: 'SoyDalto', enlace: 'https://www.youtube.com/watch?v=ELSm-G201Ls'}
]
</script>

<template>
    <ul>
        <li v-for="(item,index) in educacion" :key="index" :style="{ '--fecha-color': fechaColor[index].color}">
            <div class="fecha">{{ item.fecha }}</div>
            <h3 class="tittle">{{ item.title }}</h3>
            <div class="descripcion">{{ item.descripcion }}</div>
            <a class="enlace" :href="item.enlace" target="_blank">Saber más</a>
        </li>
    </ul>
</template>

<style scoped>
/*Estilos generales*/
@import url(https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap);
/*reseteo de estilos para todos los elementos y pseudo-elementos*/
*,
*::before,
*::after {
    margin: 0; /*elimina el margen predeterminado*/
    padding: 0; /*elimina el padding predeterminado*/
    box-sizing: border-box; /*incluye el padding y el borde en el tamaño total del elemento*/
}
/*Estilo para el cuerpo de la página*/
body{
    --color:rgb(30, 30, 30); /*variable para el color de texto */
    --bgColor: rgb(245, 245, 245); /*variable para el color de fondo */
    min-height: 100vh; /*asegura que el curpo ocupe al menos el 100% de la altura de la ventana*/
    display: grid; /*utiliza el modelo de caja de cuadrícula*/
    align-content: center; /*centra verticalmente el contenido dentro de la cudrícula*/
    gap: 2rem; /*espaciado entre los elemntos de la cudrícula*/
    padding: 2rem;/*espaciado interno alrededor del cuerpo*/
    font-family: "Poppins", sans-serif; /*fuente para todo el texto en la página*/
    color: var(--color); /*aplica el color de texto definido en la variable*/
    background: var(--bgColor); /*aplica el color de fondo definido en la variable*/
}

/*Estilos para la lista*/
ul {
    margin-top: 2 rem;
    --col-gap: 2rem; /*espaciado entre las columnas de la cudrícula*/
    --row-gap: 2rem; /*espaciado entre las filas de la cuadrícula*/
    --line-w: 0.25rem; /*ancho de la línea que conecta los elementos de la lista*/
    display: grid; /*usa un layout de cadrícula*/
    grid-template-columns: var(--line-w) 1fr; /*define las columans de la cuadrícula:la primera es la línea y la segunda el contenido*/
    grid-auto-columns: max-content; /*las columnas se ajustan automáticamente al contenido*/
    column-gap: var(--col-gap); /*espacio entre las columnas*/
    list-style: none; /*elimina las viñetas predeterminadas de la lista*/
    width: min(60rem, 90%); /*limita el ancho de la lista al mínimo entre 60rem y el 90% del ancho de la ventana*/
    margin-inline: auto; /*centra la lista horizontalmente*/
}

/*Estilo para la línea vertical que conecta los elementos de la lista*/
ul::before {
    content: ""; /*elemento vacío para crear la línea*/
    grid-column: 1; /*coloca la línea en la primera columna de la cudrícula*/
    grid-row: 1 / span 20; /*la línea se extiende sobre varias filas*/
    background: rgba(225, 225, 225, 0.342); /*color de la línea*/
    border-radius: calc(var(--line-w) / 2 ); /*bordes redondeados para la línea*/
}

/*Estilo para los elementos de la lista que no son el último*/
ul li:not(:last-child){
    margin-bottom: var(--row-gap); /*espacio entre los elementos de la lista*/
}

/*Estilo para cada item de la lista*/
ul li {
    grid-column: 2; /*coloca el contenido en la segunda columna de la cuadrícula*/
    --inlineP: 1.5rem; /*espacio interno horizontal dentro de cada item*/
    margin-inline: var(--inlineP); /*margen horizontal para los ítems*/
    grid-row: span 2; /*cada ítem ocupa dpsfilas en la cuadrícula*/
    display: grid; /*una un layout de cuadrícula dentro de cada ítem*/
    grid-template-rows: min-content min-content min-content; /*define tres filas de altura mínima*/
}

/*Estilo para la fecha dentro de cada ítem*/
ul li .fecha {
    --dateH: 3rem; /*altura de la sección de la fecha*/
    height: var(--dateH); /*aplica la altura definida*/
    margin-inline: calc(var(--inlineP) * -1); /*ajusta el margen horizontal para que la fecha sobresalga*/
    text-align: center; /*centra el texto dentro de la fecha*/
    background-color: var(--fecha-color); /*color de fondo, usando una variable personalizada*/
    color: white; /*color del texto en la fecha*/
    font-size: 1.25rem; /*tamaño del texto*/
    font-weight: 700; /*hace el texto en negrita*/
    display: grid; /*usa un layout de cuadrícula*/
    place-content: center; /*centra el contenido de la fecha*/
    position: relative; /*posiciona la fecha relativa a su contenedor*/
    border-radius: calc(var(--dateH) / 2 ) 0 0 calc(var(--dateH) / 2); /*bordes redondeados para la fecha*/
}
/*Estilo para parte inferior de la fecha, que parece un triángulo*/
ul li .fecha::before {
    content: ""; /*elemento vacío para crear el triángulo*/
    width: var(--inlineP); /*ancho igual al espacio interno definido*/
    aspect-ratio: 1; /*mantiene una relación de aspecto 1:1 para crear un cuadrado*/
    background: var(--fecha-color); /*usa el color de fondo de la fecha*/
    background-image: linear-gradient(rgba(0, 0, 0, 0.2) 100%, transparent); /*aplica un degradado sutil para dar un efecto de sombra*/
    position: absolute; /*posiciona el triángulo respecto al contenedor de la fecha*/
    top: 100%; /*coloca el triángulo justo debajo de la fecha*/
    clip-path: polygon(0 0, 100% 0, 0 100%); /*recorta el cuadrado para convertirlo en un triángulo*/
    right: 0; /*alinea el triángulo a la derecha de la fecha*/
}
/*Estilo para el círculo que conecta la fecha con la línea*/
ul li .fecha::after {
    content: ""; /*elemento vacío para crear el círculo*/
    position: absolute; /*posiciona el círculo respecto al contenedor de la fecha*/
    width: 1rem; /*ancho del círculo*/
    aspect-ratio: 1; /*mantiene una relación de aspecto 1:1 para crear un círculo*/
    background: var(--bgColor); /*color de fonde,utilizando la variable definida*/
    border: 0.3rem solid var(--fecha-color); /*borde del círculo con el color de la fecha*/
    border-radius: 50%; /*centra verticalmente el círculo dentro para alinearlo correctamente*/
    top: 50%; /*centra verticalmente el círculo dentro del contenedor de la fecha*/
    transform: translate(50%, - 50%); /*ajusta la posición del círculo para alinearlo correctamente*/
    right: calc(100% + var(--col-gap) + var(--line-w) / 2); /*coloca el círculo a la izq de la línea*/
}

/*Estilos para el título y la descripción dentro de cada ítem*/
ul li .title,
ul li .descripcion {
    background: var(--bgColor); /*fondo del titulo y la descripción, usando la variable definida*/
    position: relative; /*posiciona los elementos relativos a su contenedor*/
    padding-inline: 1.5rem; /*espaciado interno horizontal*/
}

ul li .title {
    overflow: hidden; /*oculta cualquier contenido que se desborde*/
    padding-block-start: 1.5rem; /*espacioado interno superior*/
    padding-block-end: 1rem; /*espaciado interno inferior*/
    font-weight: 500; /*hace el texto del título un poco mas grueso*/
}

ul li.descripcion {
    padding-block-end: 1.5rem; /*espaciado interno inferior*/
    font-weight: 300; /*hace el texto dela descripción mas delgado*/
}

/*Estilos para las sombras debajo del título y la descripción*/
ul li .title::before,
ul li .descripcion::before {
    content: ""; /*elemento vacío para crear la sombra*/
    position: absolute; /*posiciona la sombra respecto al contenedor del título o descripción*/
    width: 90%; /*ancho de la sombra*/
    height: 0.5rem; /*altura de la sombra*/
    background: rgba(0, 0, 0, 0.5); /*color de fondo oscuro para simular una sombra*/
    left: 50%; /*centra la sombra horizontalmente*/
    border-radius: 50%; /*bordes redondeados para la sombra*/
    filter: blur(4px); /*aplica un desenfoque para hacer la sombra mas suave*/
    transform: translate(-50%, 50%); /*ajusta la posición para centrar la sombra*/
}

ul li .title::before {
    bottom: calc(100% + 0.125rem); /*coloca la sombra debajo del título*/
}

ul li .descripcion::before {
    z-index: -1; /*coloca la sombra detras del contenido*/
    bottom: 0.25rem; /*coloca la sombra justo*/
}

/*Media query para pantallas anchas (40rem o más)*/
@media (min-width: 40rem){
    ul {
        grid-template-columns: 1fr var(--line-w) 1fr; /*ajusta la cuadrícula para tener tres columnas*/
    }  
    ul::before {
        grid-column: 2; /*mueve la línea vertical a la segunda columna de la cuadrícula*/
    } 
    ul li:nth-child(odd) {
        grid-column: 1; /*coloca los ítems impares en la primer columna*/
    } 
    un li:nth-child(even) {
        grid-column: 3; /*coloca losítems pares en la tercer columna*/
    }
    /*Ajuste para que el segundo ítem abarque dos filas*/
    ul li:nth-child(2) {
        grid-row: 2/4; /*el segundo ítem ocupará desde la segunda hasta la cuarta fila*/
    }

    /*Ajustes específicos para los ítems impares*/
    ul li:nth-child(odd) .fecha::before {
        clip-path: polygon(0 0, 100% 0, 100% 100%); /*invierte el triángulo en los ítems impares*/
        left: 0; /*alinea el triángulo a la izq*/
    }

    ul li:nth-child(odd) .fecha {
        border-radius: 0 calc(var(--dateH) / 2) calc(var(--dateH) / 2) 0; /*ajusta los bordes redondeados para los ítems impares*/
    }

    /*Estilo para los créditos*/
    .credits {
        margin-top: 1rem; /*espaciado superior para los créditos*/
        text-align: right; /*alinea el texto de los créditos a la derecha*/
    }
    .credits a {
        color: var(--color); /*aplica el color de texto definido en la variable*/
    }
}
</style>