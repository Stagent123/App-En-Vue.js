<template>
    <div>
        <form @submit.prevent="Enviardatos" method="post">
            <table class="table table-primary">
                <tr>
                    <td>
                        <div class="mb-3">
                            <label for="Email" class="form-label"></label>
                            <input v-model="form.Email" class="form-control" id="Email" type="text" placeholder="" aria-label="">
                        </div>
                    </td>   
                </tr>
                <tr>
                    <td>
                        <div class="mb-3">
                            <label for="password" class="form-label"></label>
                            <input v-model="form.Password"  class="form-control" id="password" type="text" placeholder="" aria-label="">
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        <div class="mb-3">
                            <label for="RePassword" class="form-label"></label>
                            <input v-model="form.RePassword" class="form-control" id="Repassword" type="text" placeholder="" aria-label="">
                        </div>
                    </td>
                </tr>
                
            </table>
        </form>
    </div>
    
    </template>

<script setup>
    import { reactive } from 'vue'; 
    import { useUsuarioStore } from '@/Api/Store';
    import axios from 'axios';
    const UsuarioStore = useUsuarioStore();

    const form = reactive({
        Email: '',
        Password: '',
        RePassword:''
    })

    async function Enviardatos() {
        if(RePassword === form.Password){
           try{
                await axios.post('http://127.0.0.1:8000/api/Usuarios/Login', {
                    email: form.Email,
                    password: form.password
                } )
                console.log('Datos Enviados Correctamente') 
            } catch(error){
                console.log('Ocurrio un error : ',error)
           }

        }
        else{
            console.log('Las contraseñas no coinciden')
        }
    }
</script>
