<script setup>
const title = "Wanda Lanatta";
const descripcion = "Técnico Universitario en Programación - UTN";
const residencia = "Ciudad de Mendoza, Mendoza, Argentina";
const presentacion = "Hola, Bienvenido a mi portafolio de proyectos.";
const redesSociales = [
  { id: 1, name: "linkedin", src: "/src/assets/linkedin_icon.svg", url: "https://www.linkedin.com/in/jose-perez/" },
  { id: 2, name: "Instagram", src: "/src/assets/instagram_icon.svg", url: "https://www.instagram.com/joseperez/" },
  { id: 3, name: "github", src: "/src/assets/github_icon.svg", url: "" },
  
 
];
const telefono = "+54 9 2604-474849";
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
      <h3>Mi Teléfono personal: {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

  <script setup>
  </script>
  
  <style scoped>
  .datos-personales {
  font-family: Arial, sans-serif;
  text-align: center;
  background-color:#DDD0C8;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.datos-personales h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 10px;
}

.datos-personales h2 {
  font-size: 1.5rem;
  color: #666;
  margin-bottom: 20px;
}

.datos-personales p {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 20px;
}

.container-list {
  list-style: none;
  padding: 0;
}

.container-list li {
  display: inline;
  margin: 0 10px;
}

.container-list a {
  text-decoration: none;
  color: #0073b1; /* LinkedIn blue */
  font-size: 1.2rem;
  transition: color 0.3s;
}

.container-list a:hover {
  color: #005582; /* Darker blue on hover */
}

.datos-personales h3, .datos-personales h4 {
  font-size: 1.2rem;
  color: #333;
  margin-top: 20px;
}
  </style>
  