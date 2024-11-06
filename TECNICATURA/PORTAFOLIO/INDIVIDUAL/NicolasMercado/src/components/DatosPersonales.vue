<script setup>
import Curriculum from "/src/assets/folder-svgrepo-com.svg";
import GitHub from "/src/assets/github-svgrepo-com.svg";
import Instagram from "/src/assets/instagram-svgrepo-com.svg";
import linkedin from "/src/assets/linkedin-1-svgrepo-com.svg";
const title = "Nicolas Mercado";
const descripcion = "Estudiante de Programacion - UTN";
const residencia = "San Rafael, Mendoza, Argentina";
const presentacion = "Hola, Bienvenid@ a mi portafolio de proyectos, soy un futuro desarrollador de paginas Web";
const redesSociales = [
  { id: 1, name: "linkedin", src: linkedin, url: "https://www.linkedin.com/in/nicol%C3%A1s-mercado-328445266/" },
  { id: 2, name: "instagram", src: Instagram, url: "https://www.instagram.com/nico_exe_mercado/?hl=es" },
  { id: 3, name: "github", src: GitHub, url: "https://github.com/NicolasMercado1" },
  { id: 4, name: "curriculum", src: Curriculum, url: "https://nicolasexemercado.netlify.app" }
];
const telefono = "+54 9 260 464-8140";
</script>

<template>
<section class="datos-personales">
  <div class="card">
    <h1>{{ title }}</h1>
    <h2>{{ descripcion }}</h2>
    <p>{{ presentacion }}</p>
    <ul class="container-lista">
      <li v-for="red in redesSociales" :key="red.id">
        <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
      </li>
    </ul>
    <h3>{{ telefono }}</h3>
    <h4>{{ residencia }}</h4>
  </div>
</section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
  text-align: center;
  color:grey;
}
p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color:grey;
  text-align: center;
}
.card {
  background-color: rgb(28, 41, 52);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
}
.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}
.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 58%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(95, 124, 285, 0.934);
}
.icon-redsocial:hover {
  background-color: rgb(28, 41, 52);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}
h3 {
  font-size: 1.2rem;
  font-weight: 680;
}
h4 {
  color:grey;
}
</style>
