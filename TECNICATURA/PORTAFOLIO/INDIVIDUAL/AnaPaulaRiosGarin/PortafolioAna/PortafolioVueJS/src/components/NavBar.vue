<template>
  <!--Barra de Navegación-->
  <nav class="navBar">
    <div class="navBarMenu">
      <ul>
        <!--v-for: se encarga de recorrer el arreglo-->
        <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="navItem">{{ nav.nombre }}</a>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';
// Creación de un arreglo de objetos
const navegacion= ref([
  { id: 1, nombre: 'Educación', enlace: '#educacion' },
  { id: 2, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 3, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Intereses', enlace: '#intereses' }
]);
</script>

<style>
/* Estilos - Barra de Navegación*/
a {
  padding: 5px;
  color: #DDE5B6;
}

.navBar {
  background-color: #8B6E5A;
  color: #C5D397;
  padding: 0.5rem 1rem;
  align-items: center;
  border-radius: 5px;
}

.navItem {
  color: #C5D397;
  text-decoration: none;
  margin-right: 1rem;
}

.navBarMenu {
  display: flex;
  justify-content: flex-end;
}

.nav-list {
  list-style: none;
}

/* Estilo para hacer scroll suave */
html {
  scroll-behavior: smooth;
}
</style>
