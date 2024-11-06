<template>
  <div id="tsparticles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>
</template>

<script setup>
import { loadAll } from "https://cdn.jsdelivr.net/npm/@tsparticles/all@3.1.0/+esm";
import { tsParticles } from "https://cdn.jsdelivr.net/npm/@tsparticles/engine@3.1.0/+esm";
import { onMounted } from "vue";

// Función para cargar la configuración de las partículas
async function loadParticles(options) {
  await loadAll(tsParticles);
  await tsParticles.load({ id: "tsparticles", options });
}

onMounted(() => {
  const configs = {
    particles: {
      destroy: {
        mode: "split",
        split: {
          count: 1,
          factor: { value: { min: 2, max: 4 } },
          rate: { value: 100 },
          particles: {
            life: { count: 1, duration: { value: { min: 2, max: 3 } } },
            move: { speed: { min: 10, max: 15 } }
          }
        }
      },
      number: { value: 100 },
      color: {
        value: [
          "#3998D0", "#2EB6AF", "#A9BD33", "#FEC73B",
          "#F89930", "#F45623", "#D62E32", "#EB586E",
          "#9952CF", "#E8FF00", "#00FF00", "#FF6F00",
          "#FF2B7D", "#00BFFF", "#A9FF2A", "#FFFF00"
        ]
      },
      shape: { type: "circle" },
      opacity: { value: 1 },
      size: { value: { min: 10, max: 15 } },
      collisions: { enable: true, mode: "bounce" },
      move: { enable: true, speed: 3, outModes: "bounce" }
    },
    interactivity: {
      events: {
        onClick: {
          enable: true,
          mode: "pop"
        }
      }
    },
    background: { color: "#000000" }
  };

  loadParticles(configs);
});
</script>

<style scoped>
#tsparticles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}
</style>
