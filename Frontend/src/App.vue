<template>
  <div id="app" class="container mt-4">
    <h1>Prueba General de Router</h1>
    
    <!-- Navegación -->
    <nav class="mb-4">
      <router-link to="/" class="btn btn-secondary me-2">Ir a Home</router-link>
      <router-link to="/Listado/Usuarios" class="btn btn-primary">Ver Usuarios</router-link>
    </nav>

    <!-- EL MOTOR DEL ROUTER: Aquí se debe ver TODO según la URL -->
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>