import { createRouter, createWebHistory } from "vue-router";
import ListadoUsuarios from "../components/ListadoUsuarios.vue"; 
import HelloWorld from "../components/HelloWorld.vue";
import GithhubStatus from "@/components/GithhubStatus.vue";
import ListadoLibros from "@/components/ListadoLibros.vue";
import ListadoGenero from "@/components/ListadoGenero.vue";
import RegistrarGenero from "@/components/RegistrarGenero.vue";
import RegistrarLibros from "@/components/RegistrarLibros.vue";
import RegistrarUsuarios from "@/components/RegistrarUsuarios.vue";
const routes = [
    {
        path: '/',
        name: 'Home',
        component: HelloWorld        
    },
    ///Listados 
    {
        path: '/Listado/Usuarios',
        name: 'ListadoUsuarios',
        component: ListadoUsuarios
    },
    {   
        path: '/Listado/Libros',
        name: 'ListadoLibros',
        component: ListadoLibros
    },
    {
        path: '/Listado/Genero',
        name: 'ListadoGenero',
        component: ListadoGenero
    },
    {
        path: '/Github/Status',
        name: 'Githubstatus',
        component: GithhubStatus
    },
    /// Registrar y Modificar Genero
    { /// Router link con props Generado para Modificar Generos usando el mismo componente registrar
        path: '/Registrar/Genero',
        name: 'RegistrarGenero',
        component: RegistrarGenero,
        props: {modo: 'crear'}
    },
    {
        path: '/Modificar/Genero/:id',
        name: 'ModificarGenero',
        component: RegistrarGenero,
        props: route =>({
            modo: 'editar',
            id: route.params.id
        })
    },
    {
        path: '/Registrar/Libros',
        name: 'RegistrarLibro',
        component: RegistrarLibros,
        props: {modo: 'crear'}
    },
    {  
        path: '/Modificar/Libros/:id',
        name: 'ModificarLibros',
        component: RegistrarLibros,
        props: route =>({
            modo: 'editar',
            id: route.params.id
        })
    },
    {
        path: '/Registrar/Usuarios',
        name: 'RegistrarUsuarios',
        component: RegistrarUsuarios,
        props: { modo: 'crear'}
    },
    {
        path: '/Modificar/Usuarios/:id',
        name: 'ModificarUsuarios',
        component: RegistrarUsuarios,
        props: route => ({
            modo: 'editar',
            id: route.params.id
        })
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router