<template>
<div>
    <ul v-if="Datos_Recibidos && Datos_Recibidos.length >= 1">
        <li v-for="Usuario in Datos_Recibidos" :key ="Usuario.id"  >
            <div class="card" style="width: 200px;">
                <img class="card-img-top" src="#" alt="Card image cap">
                <div class="card-body">
                    <h5> Enzito {{ Usuario.nombre }}</h5>
                    <p class="card-text">{{ Usuario.email }}</p>
                    <a href="#" class="btn btn-primary">{{ Usuario.telefono }}</a>
                </div>
            </div>
        </li>
        
    </ul>
    </div>
</template>


<script>
import axios from 'axios';
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
                const response = await axios.get('http://127.0.0.1:8000/api/Usuarios/Usuario/') 
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