<template>
    <div class="Principal">
        <div class="recuadro">
        <div>
            <h1> Iniciar Sesion </h1>
        </div>
        <form @submit.prevent="Enviardatos" method="post">
            <table  class="table table-primary">
                <tbody>
                    <tr>
                        <td>
                            <div class="mb-3">
                                <label for="Email" class="form-label"> Ingrese su Email</label>
                                <input v-model="form.Email" class="form-control" id="Email" type="text" placeholder="" aria-label="">
                            </div>
                        </td>   
                    </tr>
                    <tr>
                        <td>
                            <div class="mb-3">
                                <label for="password" class="form-label" >Ingrese su Contraseña</label>
                                <input v-model="form.Password"  class="form-control" id="password" type="text" placeholder="" aria-label="">
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="mb-3">
                                <label for="RePassword" class="form-label">Confirme su Contraseña</label>
                                <input v-model="form.RePassword" class="form-control" id="RePassword" type="text" placeholder="" aria-label="">
                            </div>
                        </td>

                    </tr>
                    <tr>
                        <td class="botones">
                            <button type="submit" class="btn btn-primary">Enviar</button>
                            <button type="button" @click="cams" class="btn btn-primary">Ir a Registro</button> 
                        </td>
                    </tr>
                </tbody>
            </table>
        </form>
    </div>
    </div>
    
    </template>

<script setup>
    import { reactive } from 'vue'; 
    import { useUsuarioStore } from '@/Api/Store';
    import { useRouter } from 'vue-router';
    import { api } from "@/servicios/api"
    const router = useRouter();
    const form = reactive({
        Email: '',
        Password: '',
        RePassword:''
    })
    const UsuarioStore = useUsuarioStore();
    async function Enviardatos() {
        if(form.RePassword === form.Password){
           try{
                await api.post('/Usuarios/Login/', {
                    email: form.Email,
                    password: form.Password
                } )
                console.log('Datos Enviados Correctamente')
                

            } catch(error){
                console.log('Ocurrio un error : ',error)
           }

        }
        else{
            console.log('Las contraseñas no coinciden')
        }
        buscarUsuario();
    }
    function buscarUsuario(){
        UsuarioStore.fetchUser();
    }
    function cams(){

        
        UsuarioStore.cambiar();
        router.push('/Registrar/Usuarios');
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