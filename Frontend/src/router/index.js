import { createRouter, createWebHistory } from "vue-router";
import ListadoUsuarios from "../components/ListadoUsuarios.vue"; 
import HelloWorld from "../components/HelloWorld.vue";
const routes = [
    {
        path: '/',
        name: 'Home',
        component: HelloWorld        
    },
    {
        path: '/Listado/Usuarios',
        name: 'ListadoUsuarios',
        component: ListadoUsuarios
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router