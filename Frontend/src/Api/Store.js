import { defineStore } from "pinia";

export const useUsuarioStore = defineStore('Users',{
    state:() => {
        return {
            user: {
                id: null,
                nombre: '',
                rol: 'ninguno',
                foto: null,
                prestamos: false,
                is_superuser: false
            },
            autenticado: false,
            cargando: true,
        }
    },
    getters: {
        role: (state) => state.user?.rol || null,
        isAdmin: (state) => state.user?.is_superuser || false,
    },
    actions: {
    async fetchUser() {
      this.loading = true
      try {
        const response = await api.get('/Usuarios/Auth/')
        this.user = response.data
        this.autenticado = true
      } catch (error) {
        this.user = null
        this.autenticado = false
      } finally {
        this.cargando = false
      }
    },

    async logout() {
      try {
        await api.post('/Usuarios/Logout/')
      } finally {
        this.user = null
        this.autenticado = false
      }
    }
  }
})
