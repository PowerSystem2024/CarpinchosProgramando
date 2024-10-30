<script setup>


import LinkedIn from "/src/assets/linkedin_icon.svg";
import Instagram from "/src/assets/instagram_icon.svg";
import GitHub from "/src/assets/github_icon.svg";
import Curriculum from "/src/assets/cv_resume_icon.svg";



const tittle = "Wanda Lanatta";
const descripcion = "Tecnico Universitario en Programacion - UTN";
const residencia = "Mendoza, Ciudad de Mendoza, Argentina";
const presentacion = "Hola, bienvenido a mi portafolio de proyectos.";
const redesSociales = [
    {id: 1, name: "LinkedIn", src: LinkedIn , url: 'https://www.linkedin.com/WandaLanatta/'},
    {id: 2, name: "Instagram", src: Instagram , url: 'https://www.instagram.com/wanda.oriana/'},
    {id: 3, name: "GitHub", src: GitHub, url: 'https://github.com/wandaoriana'},
    {id: 4, name: "Curriculum", src: Curriculum, url: ' '},           
];
const telefono =  "+541133146155";
</script>

<template>
    <section class="datos-personales">
        <div class="card">
            <h1>{{ tittle }}</h1>
            <h2>{{descripcion}}</h2>
            <p>{{presentacion}}</p>
            <ul class="container-lista">
                <li v-for="red in redesSociales" :key="red.id">
                    <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
                </li>
            </ul>
            <h3>Mi telefono personal: {{telefono}}</h3>
            <h4>{{residencia}}</h4>
        </div>

    </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  background-color: #bdd6d2;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
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
  background-color: #e3e5d7;
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgb(95, 124, 205, 0.934);
}

.icon-redsocial:hover{
  background-color: #858585;
  box-shadow: 0 0 5px rgb(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>