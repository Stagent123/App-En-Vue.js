<script setup>
import { ref, onMounted } from 'vue'
import { api } from "@/servicios/api"

const events = ref([])
const loading = ref(true)

const fetchGitHubEvents = async () => {
  try {
    const response = await api.get('/Github/')
    events.value = response.data
  } catch (error) {
    console.error("Error al cargar eventos de GitHub:", error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchGitHubEvents()
})
</script>

<template>
  <div class="p-6">
    <h2 class="text-xl font-bold mb-4">Historial de Webhooks de GitHub</h2>
    <div v-if="loading">Cargando eventos...</div>
    <ul v-else class="space-y-3">
      <li v-for="event in events" :key="event.id" class="border p-4 rounded shadow-sm">
        <span class="font-semibold text-blue-600">[{{ event.event_type.toUpperCase() }}]</span> 
        Repositorio: <strong>{{ event.repository }}</strong> 
        por <span class="italic">{{ event.sender }}</span> 
        <span class="text-gray-500 text-sm float-right">{{ new Date(event.created_at).toLocaleString() }}</span>
      </li>
    </ul>
  </div>
</template>