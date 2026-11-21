<template>
    <div>
        <table v-if="DatosRecibidos >= 1">
            <thead>
                <tr>
                    <td> ID     </td>
                    <td> Nombre </td>
                    <td> Modificar </td>
                    <td> Borrar </td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Genero in DatosRecibidos">
                    <td> {{ Genero.id }}   </td>
                    <td> {{ Genero.nombre  }} </td>
                    <td> ///Router Link Escrito Correctamente con Props incluidos
                        <router-link :to="{ name: 'ModificarGenero', params: { id: Genero.id }}"> Modificar Genero </router-link> 
                    </td>
                    <td> <button @click="BorrarGenero(Genero.nombre, Genero.id )"> Eliminar </button> </td>
                </tr>
            </tbody>
        </table>
        <p v-else> No Existen Generos</p>
    </div>
</template>

<script>
    import { api } from "@/servicios/api"
    export default {
        name: ListadoGenero,
        data(){
            return{
                DatosRecibidos: []
            }
        },
        mounted() {
            this.BuscarGeneros()
        },
        methods:{
            async BuscarGeneros(){
                try {
                    const Respuesta = await api.get('/Biblioteca/Generos/')
                    if (Respuesta.data.length >= 1){
                        console.log('Se encontraron Generos')
                        this.DatosRecibidos = Respuesta
                    }
                    else{
                        console.log('No se han encontrado Generos cargados')
                    }
                } catch(error){
                    console.log('Error', error)
                }
            },
            async BorrarGenero(dato,id){
                const respuestapre = confirm(`¿Usted quiere borrar el Genero "${dato}"?`)
                if (respuestapre === true){
                    try{
                        const Respuesta = await api.delete(`/Biblioteca/Generos/${id}`)
                        if (Respuesta.status >= 200 && Respuesta.status < 300) {
                            console.log('Error', error)
                            this.BuscarGeneros()
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