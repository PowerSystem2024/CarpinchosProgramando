<script setup>
import NavBar from './components/navBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';

</script>

<template>
  <header>
      <!--Barra de Navegacion-->
      <NavBar />
      <!--Componente Datos Personales-->    
      <DatosPersonales />
  </header>
  <main>
      <!--el estilo css de section se encuentra en base.css-->
      <section id="educacion"><h3>Educación - Cursos</h3>
      <Educacion />
      </section>
      <section id="experiencia"><h3>Experiencia</h3></section>
      <section id="proyectos"><h3>Proyectos</h3></section>
      <section id="habilidades"><h3>Habilidades</h3></section>
      <section id="intereses"><h3>Intereses</h3></section>
  </main>
</template>


<style scoped>



</style>
