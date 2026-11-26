<template>
    <div class="Principal">
        <div class="recuadro">
            <div>
                <h1> {{ tituloVista }}</h1>
            </div>
            <div class="table table-primary">
                <form id="Usuario" @submit.prevent="enviardatos" method="post">
                    <table >
                        <thead> 
                            <tr>
                                <td>
                                        <h1> Datos del Usuario</h1>
                                </td>
                            </tr>
                        </thead>
                        <tbody>
                            <tr> 
                                <td>
                                    <input type="text" v-model="form.nombre" class="Formulario_Inputs" id="NombreFloating" placeholder="Escriba Su Nombre" value="Nombre de Ejemplo" >
                                    <label for="NombreFloating"> Ingrese su Nombre </label>
                                </td>
                            </tr>
                            <tr> 
                                <td>
                                    <input type="email" v-model="form.email" class="Formulario_Inputs" id="EmailFloating" placeholder="Escriba Su Email" value="Ejemplo@email.com" > 
                                    <label for="EmailFloating"> Ingrese su Email </label>
                                </td>
                            </tr>
                            <tr> 
                                <td>
                                    <input type="number" v-model="form.telefono" class="Formulario_Inputs" id="TelefonoFloating" placeholder="Escriba Su Telefono" value="99188213" >  
                                    <label for="TelefonoFloating"> Ingrese su numero de Telefono </label>
                                </td>
                            </tr>
                            <tr> 
                                <td>
                                    <input type="password" v-model="form.password" class="Formulario_Inputs" id="PasswordFloating" placeholder="Escriba Su Password" value="1234Password" >  
                                    <label for="PasswordFloating"> Ingrese su Contraseña </label>
                                </td>
                            </tr>
                            <tr> 
                                <td>
                                    <input type="password" v-model="repassword" class="Formulario_Inputs" id="RePasswordFloating" placeholder="Repita Su Password" value="1234Password" >  
                                    <label for="PasswordFloating"> Ingrese su Contraseña </label>
                                </td>
                            </tr>
                            <tr> 
                                <td>
                                    <input type="image" v-model="form.foto" class="Formulario_Inputs" id="FotoFloating" placeholder="Foto de Perfil" value="" >  
                                    <label for="FotoFloating"> Ingrese su Foto de Perfil </label>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <button type="submit" form="Usuario" class="btn btn-primary"> Enviar </button>
                                    <button type="button" form="Usuario" @click="Reset()" class="btn btn-secondary"> Borrar </button>
                                    <button type="button" @click="volver()" class="btn btn-primary"> Volver</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>       
                </form>  
            </div>
        </div>
    </div>
    </template>


<script>
import { api } from "@/servicios/api"
import {useUsuarioStore} from "@/Api/Store";

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
            return {
                form: {
                    nombre: '',
                    email: '',
                    password: '',
                    telefono: '',
                    foto: '',
                },
                repassword:''
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
            volver(){
                const UsuarioStore = useUsuarioStore();
                UsuarioStore.cambiar();
                this.$router.push('/Home');
                },
            async enviardatos(){
                if (this.form.password === this.repassword) {
                    try {
                        const response = await api.post('/Usuarios/Usuario/', this.form.data) 
                        this.Reset();
                        const UsuarioStore = useUsuarioStore();
                        confirm(`Datos obtenidos correctamente, estos son los datos: ${JSON.stringify(response.data)} `)
                        UsuarioStore.cambiar();
                        await this.$router.push('/')
                    } catch (error) {
                        console.log("Error",error);
                    }
                }
            },
            Reset(){
                this.form.nombre = '';
                this.form.email = '';
                this.form.password = '';
                this.form.telefono = '';
                this.form.foto = '';
                this.repassword = '';
            },
            async obtenerDatosGenero(){
                try {
                    const response = await api.get(`/Usuarios/Usuario/${this.id}`) 
                    if (response.data.length >= 1 ){
                        this.form = response.data;
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

<style>
    .Principal{
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 90vh;
    }
    .table{
        width: 100%;

    }
    .recuadro{
        width: 50%;
    }
    .btn{
        margin-right: 15px;
    }
    h1{
        text-align: center;
    }
    .botones{
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>