// App-vue - Es la aplicación principal del portafolio web

// SCRIPT - JavaScript
// setup - Se ejecuta cuando se crea un componente y se utiliza para inicializar y 
//         configurar el componente en Vue
//       - Es una de las funciones más importantes de la API de composición en Vue 3
<script setup>
  import NavBar from './components/NavBar.vue';
  import DatosPersonales from './components/DatosPersonales.vue';
  import Educacion from './components/ComponenteEducacion.vue';
  import Experiencia from './components/ComponenteExperiencia.vue';
  import Proyectos from './components/ComponenteProyectos.vue';
  import Habilidades from './components/ComponenteHabilidades.vue';
  import Intereses from './components/ComponenteIntereses.vue';
</script>

// TEMPLATE - HTML
<template>
  <!--Dentro de 'template', los comentarios son como en HTML-->

  <!--Funcionamiento de Vue composition Api básico-->
  <!--Hay que estructurar el código, teniendo en cuenta el SEO Web-->

  <!--CABECERA-->
  <header id="top">
    <!--Barra de Navegación-->
    <NavBar />

    <!--Datos Personales-->
    <DatosPersonales />
  </header>

  <!--MAIN-->
  <main>
    <section id="educacion"><h2>EDUCACIÓN - CURSOS</h2>
      <Educacion />
    </section>
    <section id="experiencia"><h2>EXPERIENCIA</h2>
      <Experiencia />
    </section>
    <section id="proyectos"><h2>PROYECTOS</h2>
      <Proyectos />
    </section>
    <section id="habilidades"><h2>HABILIDADES</h2>
      <Habilidades />
    </section>
    <section id="intereses"><h2>INTERESES</h2>
      <Intereses />
    </section>
  </main>

  <footer>
    <a href="#top">Inicio</a>
    <p>© 2024 Ana Paula Ríos Garín - Portafolio Web</p>
  </footer>
</template>

// STYLE - CSS
<style scoped>
h2{
  font-weight: 700;
}

footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  font-size: 1.3rem;
  background-color: #8B6E5A;
}

footer a, p {
  color: #ADC178;
}

footer a:hover {
  text-decoration: underline;
}
</style>

// TERMINAL
// npm run dev - Modo desarrollo
