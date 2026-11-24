<template>
    <div>
        <h1> {{ this.tituloVista }}</h1>
    </div>
    <div>
        <form id="Libros" @submit.prevent="enviardatos" methods="post">
            <table>
                <tr>
                    <td>
                        <input type="text" v-model="form.Titulo" id="TituloFlotante" >
                        <label for="TituloFlotante" > Ingrese el Titulo del Libro </label>
                    </td>
                    <td>
                        <input type="text" v-model="form.Editorial" id="EditorialFlotante">
                        <label for="EditorialFlotante" >Ingrese la editorial del Libro </label>
                    </td>
                    <td>
                        <input type="Version" v-model="form.Version" id="VersionFlotante">
                        <label for="VersionFlotante" >Ingrese la Version del Libro </label>
                    </td>
                    <td>
                        <input type="text" v-model="form.Autor" id="AutorFlotante">
                        <label for="AutorFlotante" >Ingrese el nombre Autor del Libro </label>
                    </td>
                    <td>
                        <input type="number" v-model="form.Paginas" id="PaginaFlotante">
                        <label for="PaginaFlotante" >Ingrese la cantidad de Paginas </label>
                    </td>
                    <td>
                        <input type="number" v-model="form.Paginas" id="PaginaFlotante">
                        <label for="PaginaFlotante" >Ingrese la cantidad de Paginas </label>
                    </td>
                    <td>
                        <input type="image" v-model="form.Portada" id="PortadaFlotante">
                        <label for="PortadaFlotante">Agregue una imagen para usarla como Portada </label> 
                    </td>
                    <td>
                        <input type="text" v-model="form.Sinopsis" id="SinopsisFlotante">
                        <label for="SinopsisFlotante"> Agregue la sinopsis del libro</label>
                    </td>
                    ///Generos
                </tr>
                <tr>
                    <td>
                        <button type="button" form="Libros" @click="enviardatos()" class="btn btn-primary"></button>
                    </td>
                    <td>
                        <button type="button" form="Libros" @click="Reset()" class="btn btn-secondary"> Borrar </button>
                    </td>
                </tr>
            </table>
        </form>
    </div>
</template>

<script>
    import { api } from "@/servicios/api"
    export default {
        props: {
            modo: {
                type: String,
                default: 'crear'
            },
            id: {
                type: [String,Number],
                default: null
            }
        },
        data(){
            return{
                form: {
                    Titulo:'',
                    Editorial:'',
                    Version:'',
                    Paginas:0,
                    Autor: '',
                    Portada: '' ,
                    Sinopsis: '',
                    Generos: []
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
        async mounted(){
            this.obtenerDatosGenero()
        },
        methods: {
            async enviardatos(){
                try {
                    const respoonse = await api.post('/Biblioteca/Libros/', this.form)
                    this.form = {
                        titulo:'',
                        Editorial:'',
                        Version:'',
                        Paginas:0,
                        Autor: '',
                        Portada: '' ,
                        Sinopsis: '',
                        Generos: []
                    }
                    console.log("Datos Enviados", respoonse)
                } catch(error){
                    console.log("Error");
                }
            },
            Reset(){
                this.form.Titulo = '';
                this.form.Editorial = '';
                this.form.Version = '';
                this.form.Paginas = 0;
                this.form.Autor = '';
                this.form.Portada = '';
                this.form.Sinopsis = '';
                this.form.Generos = []
            },
            async obtenerDatosGenero(){
                try {
                    const response = await api.get(`/Biblioteca/Libros/${this.id}`) 
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