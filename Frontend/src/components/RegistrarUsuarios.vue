<template>
    <div>
        <h1> {{ this.tituloVista }}</h1>
    </div>
    <div>
        <form id="Usuario" @submit.prevent="enviardatos" method="post"></form>
            <table>
                <tr> 
                    <td>
                        <input type="text" v-model="form.nombre" class="Formulario_Inputs" id="NombreFloating" placeholder="Escriba Su Nombre" value="Nombre de Ejemplo" >  </input>
                        <label for="NombreFloating"> Ingrese su Nombre </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="email" v-model="form.email" class="Formulario_Inputs" id="EmailFloating" placeholder="Escriba Su Email" value="Ejemplo@email.com" >  </input>
                        <label for="EmailFloating"> Ingrese su Email </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="number" v-model="form.telefono" class="Formulario_Inputs" id="TelefonoFloating" placeholder="Escriba Su Telefono" value="99188213" >  </input>
                        <label for="TelefonoFloating"> Ingrese su numero de Telefono </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="Password" v-model="form.password" class="Formulario_Inputs" id="PasswordFloating" placeholder="Escriba Su Password" value="1234Password" >  </input>
                        <label for="PasswordFloating"> Ingrese su Contraseña </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="Password2" v-model="repassword" class="Formulario_Inputs" id="RePasswordFloating" placeholder="Repita Su Password" value="1234Password" >  </input>
                        <label for="PasswordFloating"> Ingrese su Contraseña </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="file" v-model="form.foto" class="Formulario_Inputs" id="FotoFloating" placeholder="Foto de Perfil" value="" >  </input>
                        <label for="FotoFloating"> Ingrese su Foto de Perfil </label>
                    </td>
                </tr>
                <tr>
                    <td>
                        <button type="button" form="Usuario" @click="enviardatos()" class="btn btn-primary"> Enviar </button>
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
    export default {
        name: 'RegistrarUsuarios',
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
            async enviardatos(){
                if (this.form.password === this.repassword) {
                    try {
                        const respoonse = await api.post('/Usuarios/Usuario/', this.form.data) 
                        this.Reset();
                        console.log("Datos Enviados",respoonse)
                    } catch (error) {
                        console.log("Error");
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