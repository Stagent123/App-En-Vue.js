<template>
    <div>
        <form @submit.prevent="Enviardatos" method="post">
            <table class="table table-primary">
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
                        <td>
                            <button type="submit" >Enviardatos</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </form>
    </div>
    
    </template>

<script setup>
    import { reactive } from 'vue'; 
    import { useUsuarioStore } from '@/Api/Store';
    
    import { api } from "@/servicios/api"

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
    
    



</script>
