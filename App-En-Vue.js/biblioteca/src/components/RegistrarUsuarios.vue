<template>
    <div>
        <form id="Usuario" action="enviar" method="post">         </form>
            <table>
                <tr> 
                    <td>
                        <input type="text" class="Formulario_Inputs" id="NombreFloating" placeholder="Escriba Su Nombre" value="Nombre de Ejemplo" >  </input>
                        <label for="NombreFloating"> Ingrese su Nombre </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="email" class="Formulario_Inputs" id="EmailFloating" placeholder="Escriba Su Email" value="Ejemplo@email.com" >  </input>
                        <label for="EmailFloating"> Ingrese su Email </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="number" class="Formulario_Inputs" id="TelefonoFloating" placeholder="Escriba Su Telefono" value="99188213" >  </input>
                        <label for="TelefonoFloating"> Ingrese su numero de Telefono </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="Password" class="Formulario_Inputs" id="PasswordFloating" placeholder="Escriba Su Password" value="1234Password" >  </input>
                        <label for="PasswordFloating"> Ingrese su Contraseña </label>
                    </td>
                </tr>
                <tr> 
                    <td>
                        <input type="file" class="Formulario_Inputs" id="FotoFloating" placeholder="Foto de Perfil" value="" >  </input>
                        <label for="FotoFloating"> Ingrese su Foto de Perfil </label>
                    </td>
                </tr>
            </table>        
    </div>
    </template>