<template>
  <div v-if="UsuarioStore.cargando">
    <BarraSuperior> </BarraSuperior>
  </div>
  <div id="app" class="container mt-4">
    <div v-if="UsuarioStore.autenticado === false">
        <IniciarSesion> </IniciarSesion>
        <div>
          <router-link to="RegistrarUsuario" ></router-link>
        </div>
    </div>
    
    <router-view></router-view>
  </div>
</template>

<script setup>
import BarraSuperior from './components/BarraSuperior.vue';

import IniciarSesion from './components/IniciarSesion.vue';
import { onMounted } from 'vue';
import { useUsuarioStore } from './Api/Store.js';
const UsuarioStore = useUsuarioStore();

onMounted(() =>{
  UsuarioStore.fetchUser();
})
</script>