<template>
    <div>
        <table v-if="Datos_Recibidos.length >= 1">
            <thead>
                <tr>
                    <td> ID     </td>
                    <td> Nombre </td>
                    <td> Email </td>
                    <td> Telefono </td>
                    <td> Foto </td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Usuarios in Datos_Recibidos" :key="Usuarios.id">
                    <td> {{ Usuarios.id }}   </td>
                    <td> {{ Usuarios.nombre  }} </td>
                    <td> {{ Usuarios.email  }} </td>
                    <td> {{ Usuarios.telefono  }} </td>
                    <td> <img :src="Usuarios.foto" alt="Foto del Usuario"> </td>
                    <td> ///Router Link Escrito Correctamente con Props incluidos
                        <router-link :to="{ name: 'ModificarUsuario', params: { id: Usuarios.id }}"> Modificar Usuario </router-link> 
                    </td>
                    <td> <button @click="BorrarGenero( Usuarios.nombre,Usuarios.id)"> Eliminar </button> </td>
                </tr>
            </tbody>
        </table>
        <p v-else> No Existen Usuarios</p>
    </div>
</template>


<script>

import { api } from "@/servicios/api"
export default {
    name: 'ListadoUsuarios',
    data (){ 
        return {
        Datos_Recibidos: []
        }
    }
    ,
    mounted(){
        this.obtenerDatosUsuarios()
    },
    methods: {
        async obtenerDatosUsuarios(){
            try {
                const response = await api.get('/Usuarios/Usuario/') 
                if (response.data.length >= 1 ){
                    this.Datos_Recibidos = response.data
                    console.log('Datos obtenidos correctamente, estos son los datos: ',response.data)
                }
                else {
                    console.log ('No existe ningun dato para mostrar')
                }
            } catch(error){
                console.log('Error',error)
            }
            
        },
        async BorrarUsuarios(dato,id){
                const respuestapre = confirm(`¿Usted quiere borrar el libro "${dato}"?`)
                if (respuestapre === true){
                    try{
                        const Respuesta = await api.delete(`/Biblioteca/Usuarios/Usuario/${id}`)
                        if (Respuesta.status >= 200 && Respuesta.status < 300) {
                            console.log('Error', Respuesta.error)
                            this.obtenerDatosLibros()
                        }
                        else{
                            console.log('No se Encontro Genero para Borrar')
                        }
                    }catch (error) {
                        console.log('Error',error)
                    }    
                }            
            }
    }

    
}
</script>