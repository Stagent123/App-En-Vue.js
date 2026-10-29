<template>
    <div>
        <table>
                <tr>
                    <div>
                        <router-link to="/home" class="btn btn-primary me-2"> Inicio/Home </router-link>
                    </div>
                    <div class="dropdown">
                        <button class="btn btn-primary dropdown-toggle" type="button" id="Libro" data-bs-toggle="dropdown" aria-expanded="false">
                            Libros
                        </button>
                        <ul class="dropdown-menu" aria-labelledby="Libros">
                            <li>
                                <router-link to="/" class="btn btn-primary me-2"> Registrar Libro </router-link>
                            </li>
                            <li>
                                <router-link to="/" class="btn btn-primary me-2"> Listar Libros  </router-link>
                            </li>
                        </ul>
                    </div>
                    <div class="dropdown">
                        <button class="btn btn-primary dropdown-toggle" type="button" id="Inventario" data-bs-toggle="dropdown" aria-expanded="false">
                            Inventario
                        </button>
                        <ul class="dropdown-menu" aria-labelledby="">
                            <li>
                                <router-link to="/" class="btn btn-primary me-2"> Listar Inventario  </router-link>
                            </li>
                            <li>
                                <router-link to="/" class="btn btn-primary me-2"> Editar Inventario  </router-link>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <div class="dropdown">
                            <button class="btn btn-primary dropdown-toggle" type="button" id="Compras" data-bs-toggle="dropdown" aria-expanded="false">
                                Compras
                            </button>
                            <ul class="dropdown-menu" aria-labelledby="">
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Hacer Compra </router-link>
                                </li>
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Listar Todas las Compras </router-link>
                                </li>
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Mostrar Tus Compras</router-link>
                                </li>
                            </ul>
                        </div>
                        <div class="dropdown">
                            <button class="btn btn-primary dropdown-toggle" type="button" id="Prestamos" data-bs-toggle="dropdown" aria-expanded="false">
                                Prestamos
                            </button>
                            <ul class="dropdown-menu" aria-labelledby="">
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Solicitar Prestamo </router-link>
                                </li>
                                <li>
                                    <router-limk to="/" class="btn btn-primary me-2"> Mostrar Mis Prestamos </router-limk>
                                </li>
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Aceptar Prestamo </router-link>
                                </li>
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Listar Prestamos </router-link>
                                </li>
                            </ul>
                        </div>
                        <div class="dropdown">
                            <button class="btn btn-primary dropdown-toggle" type="button" id="" data-bs-toggle="dropdown" aria-expanded="false">
                                Usuario
                            </button>
                            <ul class="dropdown-menu" aria-labelledby="">
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2 "> Iniciar Sesion </router-link>
                                </li>
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2 "> Registrar </router-link>
                                </li>
                                <li>
                                    <router-link to="/" class="btn btn-primary me-2"> Listar Usuarios </router-link>
                                </li>
                            </ul>
                        </div>
                    </div>         
                </tr>
        </table>
    </div>
</template>

<style>
    .table {
        width: 100%;
        height: 10%;      
    }
    .td {
        margin-left: 1px
    }

</style>