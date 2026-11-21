<template>
    <div>
        <h1> {{ this.tituloVista() }}</h1>
    </div>
    <div>
        <table v-if="Datos_Recibidos.length >= 1">
            <thead>
                <tr>
                    <td> Id     </td>
                    <td> Titulo </td>
                    <td> Editorial     </td>
                    <td> Autor </td>
                    <td> Paginas </td>
                    <td> Sinopsis </td>
                    <td> Generos</td>
                    <td> Modificar</td>
                    <td> Borrar </td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Libros in Datos_Recibidos">
                    <td> {{ Libros.id }}   </td>
                    <td> {{ Libros.titulo }}</td>
                    <td> {{ Libros.editorial  }} </td>
                    <td> {{ Libros.autor  }} </td>
                    <td> {{ Libros.paginas  }} </td>
                    <td> {{ Libros.sinopsis  }} </td>
                    <td >
                        <div v-for="generolibro in Libros.Genero">
                            <p> {{ generolibro }}</p>
                        </div>
                    </td>
                    <td> ///Router Link Escrito Correctamente con Props incluidos
                        <router-link :to="{ name: 'ModificarLibro', params: {id: Libros.id }}"> Modificar Genero </router-link> 
                    </td>
                    <td> <button @click="BorrarLibro( Libros.Titulo, Libros.Id )"> Eliminar </button> </td>
                </tr>
            </tbody>
        </table>
        <p v-else> No Existen Generos</p>
    </div>
</template>


<script>
import { api } from "@/servicios/api"
export default {
    name: 'ListadoLibros',
    data (){ 
        return {
        Datos_Recibidos: []
        }
    },
    computed:{
        esModificar(){
            return this.modo === 'editar' && Boolean(this.id);
        },
        tituloVista(){
            return this.esModificar ? 'Modificar Libro' : 'Registrar Libro'
        }

    },
    mounted(){
        this.obtenerDatosLibros()
    },
    methods: {
        async obtenerDatosLibros(){
            try {
                const response = await api.get('/Biblioteca/Libros/') 
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
        async BorrarLibro(dato,id){
                const respuestapre = confirm(`¿Usted quiere borrar el libro "${dato}"?`)
                if (respuestapre === true){
                    try{
                        const Respuesta = await api.delete(`/Biblioteca/Libros/${id}`)
                        if (Respuesta.status >= 200 && Respuesta.status < 300) {
                            console.log('Error', error)
                            this.obtenerDatosLibros()
                        }
                        else{
                            console.log('Nos se Encontro Genero para Borrar')
                        }
                    }catch (error) {
                        console.log('Error',error)
                    }    
                }            
            }
    }

    
}
</script>