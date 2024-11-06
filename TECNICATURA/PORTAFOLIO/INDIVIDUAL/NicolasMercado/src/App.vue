<script setup>
import DatosPersonales from './components/DatosPersonales.vue';
import EducacionComponente from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import InteresesComponente from './components/InteresesComponente.vue';
import NavBar from './components/NavBar.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import PuntoGravedad from './components/PuntoGravedad.vue';
</script>

<template>
  <!-- Fondo de partículas -->
  <PuntoGravedad/>

  <!-- Contenido principal del sitio -->
  <header>
    <NavBar/>
    <DatosPersonales/>
  </header>

  <main>
    <!-- Sección de educación -->
    <section id="educacion">
      <h2>Educación</h2>
      <EducacionComponente/>
    </section>

    <!-- Sección de experiencia -->
    <section id="experiencia">
      <h2>Experiencia</h2>
      <ExperienciaComponente/>
    </section>

    <!-- Sección de proyectos -->
    <section id="proyectos">
      <h2>Proyectos</h2>
      <ProyectosComponente/>
    </section>

    <!-- Sección de habilidades -->
    <section id="habilidades">
      <h2>Habilidades</h2>
      <HabilidadesComponente/>
    </section>

    <!-- Sección de intereses -->
    <section id="intereses">
      <h2>Intereses</h2>
      <InteresesComponente/>
    </section>
  </main>


<footer>
  <a href="#top">Inicio</a>
  <p>© 2024 Nicolas Exequiel Mercado - Portafolio web</p>
</footer>
</template>

<style scoped>
footer {
display: flex;
flex-direction: column;
align-items: center;
padding: 2rem;
font-size: 1.3rem;
background-color: rgba(0, 0, 0, 1.3);
}

a{
background-color: rgb(89, 82, 82);
border-radius: 5px;
width: 100px;
text-align: center;
}

a:hover{
background-color: beige;
color: black;
}

p{
color: grey;
}
</style>

