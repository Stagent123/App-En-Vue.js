<template>
    <div>
        <h1> {{ this.tituloVista }}</h1>
    </div>
    <div>
        <form id="Generos" @submit.prevent="enviardatos" method="post"></form>
        <table>
            <tr>
                <td>
                    <input type="text" v-model="form.nombre" class="Formulario_Inputs" id="NombreFloating" placeholder="Escriba el Nombre del Genero" value="Nombre de Ejemplo"> 
                    <label for="NombreFloating"> Ingrese el nombre del Genero </label>
                </td>
            </tr>
            <tr>
                <td>
                    <button type="button" form="Generos" @click="enviardatos()" class="btn btn-primary"></button>
                </td>
                <td>
                    <button type="button" form="Usuario" @click="Reset()" class="btn btn-secondary"> Borrar </button>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
    import { api } from "@/servicios/api"
    export default{
        props: {
            modo: {
                type: String,
                default:'crear'
            },
            id: {
                type: [String,Number],
                default:null
            }
        },  
        data(){
            return {
                form: {
                    nombre: ''
                }
            }
        },
        computed:{
            esModificar(){
                return this.modo === 'editar' && Boolean(this.id);
            },
            tituloVista(){
                return this.esModificar ? 'Modificar Genero' : 'Registrar Genero'
            }
        },
        async mounted() {
            this.obtenerDatosLibros();
        },  
        watch: {
            id(){
                if(this.esModificar){
                    this.obtenerDatosGenero()
                }
                else{
                    this.Reset()
                }
            }
        },
        methods: {
            async enviardatos(){
                try{
                    if(this.esModificar){
                        const response = await api.put(`/Biblioteca/Genero/${this.id}`,this.form)
                        this.Reset()
                        console.log(response)
                    }
                    else{
                        const respoonse = await api.post('/Biblioteca/Genero/', this.form)
                        this.Reset()
                        console.log(respoonse)
                    }
                } catch (error) {
                    console.log("Error",error)
                }
            }, 
            Reset(){
                this.form.nombre = '';
            },
            async obtenerDatosGenero(){
                try {
                    const response = await api.get(`/Biblioteca/Genero/${this.id}`) 
                    if (response.data.length >= 1 ){
                        this.form = response.data
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