import { createRouter, createWebHistory } from "vue-router";
import ListadoUsuarios from "../components/ListadoUsuarios.vue"; 
import HelloWorld from "../components/HelloWorld.vue";
import GithhubStatus from "@/components/GithhubStatus.vue";
import ModificarGenero from '@/components/ModificarGenero.vue'
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
    },
    {
        path: '/Github/Status',
        name: 'Githubstatus',
        component: GithhubStatus
    },
    { /// Router link con props Generado para Modificar Generos
        path: '/Generos/Modificar',
        name: 'ModificarGenero',
        component: ModificarGenero,
        Props: true
    }   
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router