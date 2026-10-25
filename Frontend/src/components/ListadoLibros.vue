<template>
<div>
    <ul v-if="Datos_Recibidos && Datos_Recibidos.length >= 1">
        <li v-for="Libros in Datos_Recibidos" :key ="Libros.id"  >
            <div class="card" style="width: 200px;">
                <img class="card-img-top" src="#" alt="Card image cap">
                <div class="card-body">
                    <h5> Enzito {{ Libros.Titulo }}</h5>
                    <p class="card-text">{{ Libros.Editorial }}</p>
                    <p class="card-text">{{ Libros.Autor }}</p>
                    <p class="card-text">{{ Libros.Paginas }}</p>
                    <p class="card-text">{{ Libros.Sinopsis }}</p>
                    <div v-for="Genero in Libros.Generos">
                        <p class="card-text">{{ Genero }}</p>
                    </div>
                </div>
            </div>
        </li>
        
    </ul>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'ListadoLibros',
    data (){ 
        return {
        Datos_Recibidos: []
        }
    }
    ,
    mounted(){
        this.obtenerDatosLibros()
    },
    methods: {
        async obtenerDatosLibros(){
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/Biblioteca/Libros/') 
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
            
        }
    }

    
}
</script>