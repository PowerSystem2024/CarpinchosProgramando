<script setup> // setup: indica que se va a ejecutar solamente el codigo que se encuentra dentro de este script
  import NavBar from './components/icons/NavBar.vue';
</script>

<template>

  <header>
    <!-- Barra de Navegacion -->
     <NavBar />

  </header>

  <main>
      <section id="educacion"><h2>Educacion - Cursos</h2></section>
      <section id="experiencia"><h2>Experiencia</h2></section>
      <section id="proyectos"><h2>Proyectos</h2></section>
      <section id="habilidades"><h2>Habilidades</h2></section>
      <section id="intereses"><h2>Intereses</h2></section>
  </main>

</template>

<style scoped>

</style>
