<template>
      <!--Barra de Navegacion-->
      <nav class="navbar">
        <div class="navbar-menu">
            <ul>
                <nav class="navbar">
            <div class="navbar-menu">
                <ul>
                  
                    <a v-for="nav in navegacion" :key="nav.nombre" href="nav.enlace" class="nav-item" >{{nav.nombre}}</a>  
                </ul>
            </div>
</nav>

            </ul>
        </div>
    </nav>
</template>

<script setup>
import { ref } from 'vue';
const navegacion= ref([
    {id:1, nombre:'Educación', enlace:'#educacion'},
    {id:2, nombre:'Experiencia', enlace:'#experiencia'},
    {id:3, nombre:'Proyectos', enlace:'#proyectos'},
    {id:4, nombre:'Habilidades', enlace:'#habilidades'}
]);


</script>
<style scoped>
navbar {
    background-color:var(--vt-c-indigo);
    color: #DDD0C8;
    padding: 0.5rem 1rem;
    align-items: center;
  }
.navbar-item {
    color: #2d2121;
    text-decoration: none;
    margin-right: 1rem;
}
.navbar-menu {
  display: flex;
  justify-content: flex-end;
}
.nav-list{
  list-style: none;
  a {
  border: 1px solid ;
  border-color: hsla(160, 100%, 37%, 0.2);
  border-radius: 5px;
  /* Elimina la subrayado de los enlaces y elementos con clase "green" */
  text-decoration: none;
  /* Añade una transición suave para los cambios de estilo */
  transition: 0.4s;
  /* Añade padding alrededor del contenido */
  padding: 5px;
}

a:hover {
    /* Cambia el color de fondo al pasar el mouse sobre un enlace */
    background-color: hsla(160, 100%, 37%, 0.2);
}
}

@media (max-width: 768px) {
  .navbar-menu {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}
}

/* Estilos para la navegación */
nav {
  background-color:#DDD0C8;
  padding: 1rem;
  border-radius: 10px;
}

nav ul {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: space-around;
}

nav ul li {
  margin: 0 1rem; /* Añade margen horizontal entre los elementos */
}

nav ul li a {
  text-decoration: none;
  color: #007bff;
  font-weight: bold;
  transition: color 0.3s ease;
}

nav ul li a:hover {
  color: #0056b3;
}



</style>