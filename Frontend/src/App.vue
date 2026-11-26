<template>
  <div v-if="UsuarioStore.cargando">
    <BarraSuperior> </BarraSuperior>
    <div>
      <GithhubStatus></GithhubStatus>
    </div>
  </div>
  <div id="app" class="container mt-4">
    <div v-if="!UsuarioStore.autenticado ">
        <div v-if="UsuarioStore.mostrarlogin ">
          
          <IniciarSesion></IniciarSesion>
        </div>
        <div>
          <span>Estado: {{ UsuarioStore.mostrarlogin }}</span>
          <button type="button" @click="cams" class="btn btn-primary">Ir a Registro</button> 
        </div> 
    </div>
    
    <router-view></router-view>
  </div>
</template>

<script setup>
import BarraSuperior from './components/BarraSuperior.vue';
import IniciarSesion from './components/IniciarSesion.vue';
import { onMounted } from 'vue';
import { useUsuarioStore } from '@/Api/Store';
import GithhubStatus from './components/GithhubStatus.vue';
import { useRouter } from 'vue-router';
const router = useRouter();
const UsuarioStore = useUsuarioStore();

onMounted(() =>{
  UsuarioStore.fetchUser();
})
function cams(){

  UsuarioStore.cambiar();
  router.push('/Registrar/Usuarios');
 }

</script>