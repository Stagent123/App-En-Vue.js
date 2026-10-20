<template>
    <div>
        <form id="Usuario" @submit.prevent="enviardatos" method="post">         </form>
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
                        <button > Enviar </button>
                    </td>
                    <td>
                        <button > Borrar </button>
                    </td>

                </tr>
            </table>        
    </div>
    </template>


<script>
    import Axios from 'axios'
    export default {
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
        methods: {
            async enviardatos(){
                if (this.form.password === this.repassword) {
                    try {
                        const respoonse = await axios #Url
                        this.form = {
                            nombre: '',
                            email: '',
                            password: '',
                            telefono: '',
                            foto: '',
                        }
                        console.log("Datos Enviados")
                    } catch (error) {
                        console.log("Error");
                        

                    }
                }
            }
        }
    }


</script>