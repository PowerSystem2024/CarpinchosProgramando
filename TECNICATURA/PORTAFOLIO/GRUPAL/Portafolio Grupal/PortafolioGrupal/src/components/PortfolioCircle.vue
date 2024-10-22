<template>
  <div>
    <h1 class="title">Portafolios Carpinchos Programando</h1>
    <div class="circle">
      <div
        v-for="(student, index) in students"
        :key="index"
        :style="getNodeStyle(index)"
        class="node"
      >
        <div :style="getNodeColor(index)" class="node-circle"></div>
        <a :href="student.portfolio"
          class="node-link"
          :style="getLinkStyle(index, index)">{{ student.name }}</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const students = ref([
  { name: "Aguilar, Melina Elizabeth", portfolio: "/portafolio1" },
  { name: "Aguilera, Mariana Florencia", portfolio: "/portafolio2" },
  { name: "Atim, Maria Mercedes", portfolio: "/portafolio3" },
  { name: "Lanatta, Wanda Oriana", portfolio: "/portafolio4" },
  { name: "Mercado, Nicolas Exequiel", portfolio: "/portafolio5" },
  { name: "Rios, Nelson Omar", portfolio: "/portafolio6" },
  { name: "Rios Garin, Ana Paula", portfolio: "/portafolio7" },
]);

function getNodeStyle(index) {
  const angle = (index / students.value.length) * 2 * Math.PI;
  const radius = 150; // Radio ajustado para que los nodos estén por fuera
  const x = Math.cos(angle) * radius;
  const y = Math.sin(angle) * radius;

  return {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: `translate(${x}px, ${y}px) translate(-50%, -50%)`,
  };
}

function getNodeColor(index) {
  const colors = [
    'OrangeRed',
    'magenta',
    'GreenYellow',
    'deeppink',
    'Green',
    'aqua',
    'Chartreuse',
  ];
  return {
    backgroundColor: colors[index % colors.length],
    borderRadius: '50%',
    width: '30px',
    height: '30px',
    position: 'absolute',
    top: '-10px', // Mantener el nodo justo sobre el borde
    left: '50%',
    transform: 'translateX(-50%)',
  };
}

// Función para posicionar los enlaces más cerca de los nodos
// Función para posicionar los enlaces más cerca de los nodos
function getLinkStyle(index) {
  const angle = (index / students.value.length) * 2 * Math.PI;
  const radius = 110; // Radio ajustado para que queden más cerca
  const x = Math.cos(angle) * radius;
  const y = Math.sin(angle) * radius;

  const nodeColor = getNodeColor(index).backgroundColor; // Obtener el color del nodo

  return {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: `translate(${x}px, ${y}px) translate(-50%, -50%)`,
    backgroundColor: nodeColor, // Asignar el color del nodo al fondo del nombre
    color: 'black', // Color del texto
    padding: '5px',
    width: '120px', // Establecer un ancho fijo
    height: '90px', // Establecer una altura fija
    lineHeight: '25px', // Quitar interlineado igualando a la altura
    textAlign: 'center', // Centrar el texto horizontalmente
    borderRadius: '5px',
    textShadow: '1px 1px 2px lightgrey', // Sombra del texto
  };
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;700&family=Spectral+SC:wght@400&display=swap');

.title {
  font-family: 'Spectral SC', serif;
  text-align: center;
  font-weight: bold;
  font-size: 35px;
  margin-bottom: 180px; /* Aumentar el margen inferior para evitar superposición */
  z-index: 1;
  position: relative;
}

.circle {
  position: relative;
  width: 300px;
  height: 300px;
  margin: 20px auto 0; /* Aumentar el margen superior */
  border: 5px solid lightblue;
  border-radius: 50%;
  background-color: transparent;
}

.node {
  position: absolute;
  width: 80px;
  text-align: center;
}

.node-link {
  display: block;
  padding: 2px;
  font-family: 'Montserrat', sans-serif;
  font-weight: bolder;
  font-size: 20px; /* Ajustar tamaño de fuente para que quepa mejor */
  text-decoration: none;
}

.node-link:hover {
  opacity: 0.8; /* Efecto al pasar el ratón */
}
</style>
