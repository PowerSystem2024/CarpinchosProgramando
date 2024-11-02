<template>
    <nav class="navbar">
        <div class="navbar-menu">
            <ul>
                <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="nav-item">{{ nav.nombre }}
                </a>
            </ul>
        </div>
    </nav>
</template>

<script setup>
import { ref } from 'vue';
const navegacion= ref([
    {id:1, nombre:'Educación', enlace: '#educacion'},
    {id:2, nombre:'Experiencia', enlace: '#experiencia'},
    {id:3, nombre:'Proyectos', enlace: '#proyectos'},
    {id:4, nombre:'Habilidades', enlace: '#habilidades'},
    {id:5, nombre:'Intereses', enlace: '#intereses'}
]);
</script>

<style scoped>
.navbar {
    background-color: var(); /*Establece el color de fonde usando una variable css*/
    color: #ffffff; /*establece el color del texto en blanco*/
    padding: 0.5rem 1rem; /*añade un padding de 0.5rem arriba y abajo, y 1rem a los lados*/
    align-items: center; /*centra verticalmente los elementos dentro de la navbar*/
}

.nav-item {
    display: inline-block;
    margin-right: 1rem;
    color: grey;
    font-size: 20px;
    font-weight: bold;
}
.navbar-item {
    color: #ffffff; /*establece el color del texto en blanco*/
    text-decoration: none; /*elimina el subrayado de los enlaces*/
    margin-right: 1rem; /*añade un margen der4echo a 1rem entre los elementos*/
}

.navbar-menu {
    display: flex; /*organiza los elementos en línea usando flexbox*/
    justify-content: flex-end;
}
.nav-list {
    list-style: none;
}
</style>