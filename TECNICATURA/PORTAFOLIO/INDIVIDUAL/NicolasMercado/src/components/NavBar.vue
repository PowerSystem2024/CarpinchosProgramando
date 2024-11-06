<template>
  <nav class="navbar">
    <div class="navbar-menu">
      <ul class="nav-list">
        <li v-for="nav in navegacion" :key="nav.nombre">
          <a :href="nav.enlace" class="navbar-item">{{ nav.nombre }}</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
const navegacion = ref([
  { id: 1, nombre: "Educacion", enlace: "#educacion" },
  { id: 2, nombre: "Experiencia", enlace: "#experiencia" },
  { id: 3, nombre: "Proyectos", enlace: "#proyectos" },
  { id: 4, nombre: "Habilidades", enlace: "#habilidades" },
  { id: 5, nombre: "Intereses", enlace: "#intereses" },
]);
</script>

<style scoped>
.navbar {
  background-color: var(--vt-c-indigo);
  color: #fff;
  padding: 0.5rem 1rem;
  align-items: center;
}

.navbar-item {
  color: #fff;
  text-decoration: none;
  margin-right: 1rem;
}

.navbar-menu {
  display: flex;
  justify-content: flex-end;
}

.nav-list {
  list-style: none;
  display: flex;
  gap: 1rem;
}

a {
  border: 1px solid;
  border-color: hsla(160, 100%, 37%, 0.2);
  border-radius: 5px;
  text-decoration: none;
  transition: 0.4s;
  padding: 2px;
}

a:hover {
  background-color: hsla(160, 100%, 37%, 0.2);
}

@media (max-width: 768px) {
  .navbar-menu {
    display: flex;
    justify-content: flex-end;
    width: 100%;
  }
}
</style>

