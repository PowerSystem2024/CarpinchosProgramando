<template>
  <nav class="navbar">
          <div class="navbar-menu">
              <ul>
<!--Se coloco el operador v-bind al atributo href utilizando su minima expreción el operador : / y se soluciono el enlace a las distintas secciones-->
                  <a v-for="nav in navegacion" :key="nav.nombre" :href="nav.enlace" class="nav-item" >{{nav.nombre}}</a>  
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
  {id:4, nombre:'Habilidades', enlace:'#habilidades'},
  {id:5, nombre:'Intereses', enlace:'#intereses'}
]);
</script>

<style scoped>
.navbar {
 
  color: #fff; /* Establece el color del texto en blanco */
  padding: 0.5rem 1rem; /* Añade un padding de 0.5rem arriba y abajo, y 1rem a los lados */
  align-items: center; /* Centra verticalmente los elementos dentro de la navbar */
}

.navbar-item {
  color: #ffffff; /* Establece el color del texto en blanco */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  margin-right: 1rem; /* Añade un margen derecho de 1rem entre los elementos */
}

.navbar-menu {
  display: flex; /* Organiza los elementos en línea usando flexbox */
  justify-content: flex-end; /* Alinea los elementos al final de la navbar */
  
}

.nav-list {
  list-style: none; /* Elimina los puntos o números de las listas */

}

a {
  position: relative; /* Necesario para efectos futuros */
  color: #fff; /* Color del texto */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  margin-right: 1rem; /* Añade un margen derecho de 1rem entre los elementos */
  border-radius: 5px; /* Redondea las esquinas del borde */
  padding: 5px; /* Añade un padding de 5px alrededor del contenido */
  transition: transform 0.2s; /* Transición suave para el efecto */
}

a:hover {

  background-color: hsla(204, 100%, 58%, 0.934); /* Cambia el color de fondo al pasar el mouse sobre un enlace */
  box-shadow: 0 0 10px hsla(204, 100%, 58%, 0.934);
}

@media (max-width: 768px) {
.navbar-menu {
  display: flex; /* Organiza los elementos en línea usando flexbox */
  justify-content: center; /* Alinea los elementos al final de la navbar */
  width: 100%; /* Asegura que la navbar ocupe el 100% del ancho en pantallas pequeñas */
}
}

</style>