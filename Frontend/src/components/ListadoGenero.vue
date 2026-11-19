<template>
    <div>
        <ul v-if="DatosRecibidos >= 1">
           <li v-for="Genero in DatosRecibidos">
             <div class="card" style="width:200px;">
                <p> IDGenero: {{ Genero.Id }}</p>
                <p> Nombre: {{ Genero.Nombre }}</p>

             </div>

           </li>

        </ul>
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
            }
        }
    }
</script>