<template>
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
            </table>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
import Axios from 'axios'
    export default {
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
        methods: {
            async enviardatos(){
                try {
                    const respoonse = await axios.post('http://127.0.0.1:8000/api/Biblioteca/Generos/', this.form)
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
                    console.log("Datos Enviados")
                } catch(error){
                    console.log("Error");
                }
            }
        }
    }
</script>