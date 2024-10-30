
<script setup>
import {ref} from 'vue';
const fechaColor = ref([]);
fechaColor.value = [
    {color: '#41516c'},
    {color: '#FBCA3E'},
    {color: '#E24A68'},
    {color: '#4CADAD'}
];
const educacion = ref ([]);
educacion.value = [
    {fecha: '2024', tittle: 'Tecnicatura Universitaria en Programacion', descripcion: 'Operacion y programacion de computadoras.', enlace:'http:youtube.com'},
    {fecha: '2015', tittle: 'Ingenieria en Computacion', descripcion: 'Universidad nacional de Tucuman', enlace: 'http:youtube.com'}
]
</script>

<template> 
    <ul>
        <li v-for="(item, index) in educacion" :key="index" :style="{'--fecha-color': fechaColor[index].color}">
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="tittle">{{ item.tittle }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
        <!--Aqui vemos con el uso de b-vind (:) que bindeamos el atributo href de html con el item.enlace-->
     
        </li>
    </ul>
</template>

<style scoped>
/*Estilos generales*/
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&displau=swap");

/*reseteo de estilos basicos para todos los elementos y pseudo-elementos*/
*,
*::before,
*::after{
    margin: 0; /*Elimina el margen predeterminado*/
    padding: 0; /*Elimina el padding predeterminado*/
    box-sizing: border-box; /*Incluye el padding y el borde en el tamaño total del elemento */
}

/* Estilo para el cuerpo de la pagina*/
body{
    --color: rgba(30, 30, 30); /*Variable para el color de texto */
    --bgColor: rgba(245, 245, 245); /*Variable para el color de fondo */
    min-width: 100vh; /* Asegura que el cuerpo ocupe al menos el 100% de la altura de la ventana*/
    display: grid; /*Utiliza el modelo de caja de cuadricula */
    align-content: center; /*Centra verticalmente el contenido dentro de la cuadricula */
    gap: 2rem; /*Espaciado entre los elementos de la cuadricula */
    padding: 2rem; /*Espaciado interno alrededor del cuerpo */
    font-family: "Poppins", sans-serif; /*Fuente para todo el texto en la pagina */
    color: var(--color); /*Aplica el color de texto definido en la variable */
    background: var(--bgColor); /*Aplica el color de fondo definido en la variable*/
}

/* Estilos para la lista*/
ul{
    margin-top: 2rem;
    --col-gap: 2rem; /*Espacio entre las columnas de la cuadricula */
    --row-gap: 2rem; /*Espacio entre las filas de la cuadricula*/
    --line-w: 0.25rem;  /*Ancho de la linea que conecta los elementos de la lista */
    display: grid; /* Usa un layout de cuadricula */
    grid-template-columns: var(--line-w) 1fr; /*Define las columnas de la cuadricula: la primera es la linea y la segunda es el contenido */
    grid-auto-columns: max-content; /*Las columnas se ajustan automaticamente al contenido */
    column-gap: var(--col-gap); /*Espacio entre columnas */
    list-style: none; /*Elimine las viñetas predeterminadas de la lista */
    width: min(60rem, 90%); /* Limita el ancho de la lista al minimo entre 60rem y el 90% del ancho de la ventana*/
    margin-inline: auto; /*Centra la lista horizontalmente */
}

/*Estilo para la linea vertical que conecta los elementos de la lista */
ul::before{
    content: ""; /*Elemento vacio para crear la linea */
    grid-column: 1; /*Coloca la linea en la primera columna de la cuadricula */
    grid-row: 1 / span 20; /*La linea se extiende sobre varias filas */
    background: rgb(225,225, 225);  /*Color de la linea */
    border-radius: calc(var(--line-w) / 2);  /*Borders redondeados para la linea */
}

/*Estilos para los elementos de la lista que no son el ultimo */
ul li:not(:last-child){
    margin-bottom: var(--row-gap); /*Espacio entre los elementos de la lista */
}

/*Estilo para cada item de la lista */
ul li{
    grid-column: 2; /*Coloca el contenido en la segunda columna de la cuadricula */
    --inlineP: 1.5rem; /*Espacio interno horizontal dentro de cada item */
    margin-inline: var(--inlineP); /*Margen horizontal para los items */
    grid-row: span 2; /*Cada item ocupa dos filas en la cuadricula */
    display: grid; /*Usa un layout de cuadricula dentro de cada item */
    grid-template-rows: min-content min-content min-content; /*Define tres filas de altura minima */
}

/*Estilos para la fecha dentro de cada item */
ul li .fecha{
    --dateH: 3rem; /*Altura de la seccion de la fecha */
    height: var(--dateH); /*Aplica la altura definida */
    margin-inline: calc(var(--inlineP) * -1); /*Ajusta el margen horizontal para que la fecha sobresalga */
    text-align: center; /*Centra el texto dentro de la fecha */
    background-color: var(--fecha-color); /*Color de fondo, usando variable personalizada */
    color: white; /*Color del texto en la fecha */
    font-size: 1.25rem; /*Tamaño del texto */
    font-weight: 700;  /*Hace el texto en negrita */
    display: grid; /*Usa un layout de cuadricula */
    place-content: center;  /*Centra el contenido de la fecha */
    position: relative;  /*Posiciona la fecha realtiva a su contenedor */
    border-radius: calc(var(--dateH) / 2) 0 0 calc(var(--dateH) /2);  /*Borders redondeados para la fecha */
}

/*Estilo para la parte inferior de la fecha, que parece un triangulo */
ul li .fecha::before{
    content: ""; /*Elemento vacio para crear el triangulo */
    width: var(--inlineP); /*Ancho igual al espacio interno definido*/
    aspect-ratio: 1; /*Mantiene una relacion de aspecto 1:1 para crear un cuadrado */
    background: var(--fecha-color); /*Usa el color de fondo de la fecha*/
    background-image: linear-gradient(rgb(0, 0, 0, 0.2) 100%, transparent); /*Aplica un degradado sutil para dar un efeco de sombre */
    position: absolute; /*Posiciona el triangulo respecto al contenedor de la fecha */
    top: 100%; /*Coloca el triangulo justo debajo e la fecha */
    clip-path: polygon(0 0, 100% 0, 0 100%); /*Recorta el cuadrado para convertirlo en un triangulo */
    right: 0; /*Alinea el triangulo a la derecha de la fecha */
}

/*Estilo para el circulo que conecta la fecha con la linea  */
ul li .fecha::after{
    content: ""; /*Elemento vacio para crear el circulo */
    position: absolute; /*Posiciona el circulo respecto al contenedor de la fecha */
    width: 1rem; /*Ancho del circulo*/
    aspect-ratio: 1; /*Mantiene una relacion de aspecto 1:1 para crear un circulo */
    background: var(--bgColor); /*Usa el color de fondo*/
    border-radius: 50%; /*Hace que el elemento sea un circulo perfecto */
    top: 50%; /*Centra verticalmente el circulo dentro del contenedor de la fecha */
    transform: translate(50%, -50%);  /*Ajusta la posicion del circulo para alinealo correctamente */
    right: calc(100% + var(--col-gap) + var(--line-w) / 2); /*Coloca el circulo a la izquierda de la linea */
}

/*Estilos para el titulo y la descripcion dentro de cada item */
ul li .tittle,
ul li .descripcion{
    background: var(--bgColor); /*Fondo del titulo y la descripcion, usando la variable definida */
    position: relative; /*Posiciona los elementos relativos a su contenedor */
    padding-inline: 1.5rem; /*Espaciado interno horizontal */ 
}

ul li .tittle{
    overflow: hidden; /*Oculta cualquier contenido que se desborde */
    padding-block-start: 1rem; /*Espaciado interno superior */
    padding-inline-end: 1rem; /*Espaciado interno inferior */
    font-weight: 500; /*Hace el texto del titulo un poco mas grueso */
}

ul li .descripcion{
    padding-block-end: 1.5rem; /*Espaciado interno inferior */
    font-weight: 300; /*Hace el texto de la descripcion mas delgado */
}

/*Estilos para las sombras debajo del titulo y la descripcion */
ul li .tittle::before,
ul li .descripcion::before{
    content: "";  /*Elemento vacio para crear la sombra */
    position: absolute; /*Posiciona la sombra respecto al contenedor del titulo o descripcion */
    width: 90%; /*Ancho de la sombra */
    height: 0.5rem; /*Altura de la sombra */
    background: rgb(0, 0, 0, 0.5); /*Color de fondo oscuro para simular una sombra */
    left: 50%; /*Centra la sombra horizontalmente */
    border-radius: 50%; /*Bordes redondeados para la sombra */
    filter: blur(4px); /*Aplica un desenfoque para hacer la sombra mas suave */
    transform: translate(-50%, 50%); /*Ajusta la posicion para centrar la sombra */
}

ul li .tittle::before{
    bottom: calc(100% + 0.125rem); /*Coloca la sombra debajo del titulo */
}

ul li .descripcion::before{
    z-index: -1; /*Coloca la sombra detras del contenido */
    bottom: 0.25rem; /*Coloca la sombra justo */
}


/*Media query para pantallas anchas (40rem o mas) */
@media (min-width: 40rem){
    ul{
        grid-template-columns: 1fr var(--line-w) 1fr; /* Ajusta la cuadricula para tener tres xolumnas */
    }
    ul::before{
        grid-column: 2; /*Mueve la linea vertical a la segunda columna de la cuadricula */
    }
    ul li:nth-child(odd){
        grid-column: 1; /*Coloca los items impares en la primera columna */
    }
    ul li:nth-child(even){
        grid-column: 3; /*Coloca los items pares en la  tercera columna */
    }

    /*Ajusta para que el segundo item abarque dos filas */
    ul li:nth-child(2){
        grid-row: 2/4; /*El segundo item ocupara desde la segunda hasta la cuarta fila */
    }

    /*Ajustes especificos para los items impares */
    ul li:nth-child(odd) .fecha::before{
        clip-path: polygon(0 0, 100% 0, 100% 100%); /*Invierte el triangulo en los items impares */
        left: 0; /*Alinea el triangulo a la izquierda */
    }

    ul li:nth-child(odd) .fecha::after{
        transform: translate(-50%, -50%); /*Ajusta la posicion del circulo en los items impares */
        left: calc(100% + var(--col-gap)+ var(--line-w) /2); /*Coloca el circulo a la derecha de la linea */
    }

    ul li:nth-child(odd) .fecha{
        border-radius: 0 calc(var(--dateH)/2) calc(var(--dateH)/2) 0; /*Ajusta los bordes redondeados para lods items impares */
    }

    /*Estilo para los creditos */
    .credits{
        margin-top: 1rem; /*Espaciado superior para los creditos */
        text-align: right; /*Alinea el texto de los creditos a la derecha */
    }
    .credits a{
        color: var(--color); /*Aplica el color de texto definido e nla variable */
    }
}
</style>