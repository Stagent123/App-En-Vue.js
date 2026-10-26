<template>
    <div>
        <form id="Generos" @submit.prevent="enviardatos" method="post"></form>
        <table>
            <tr>
                <td>
                    <input type="text" v-model="form.nombre" class="Formulario_Inputs" id="NombreFloating" placeholder="Escriba el Nombre del Genero" value="Nombre de Ejemplo"> </input> 
                    <label for="NombreFloating"> Ingrese el nombre del Genero </label>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
    import Axios from 'axios'
    export default{
        data(){
            return {
                form: {
                    nombre: ''
                }
            }
        },
        methods: {
            async enviardatos(){
                try {
                    const respoonse = await Axios('http://127.0.0.1:8000/api/Biblioteca/Genero/', this.form.data)
                    this.form = {
                        nombre: ''
                    }
                } catch (error) {
                    console.log("Error",error)
                }
            }
        }
    }
    </script>