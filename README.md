# App-En-Vue.js
App creada en Vue.js (Biblioteca con API de Pago y APi de Inicio de Sesion)


consistirá en una app simple con la posibilidad de agregar Libros a la biblioteca, añadir libros a la biblioteca con la posibilidad de comprar libros o pedirlos prestados (Debe tener una cuenta) 


# Acciones 

* CRUD de Biblioteca
* Creacion de Usuarios
* Api de Pagos
* WebHook de Pagos

# Usuarios

* Gerente
* Cliente
* Cajero
* Inventario
  
# Clases

##  Inventario
- Id Del Libro
- Inventario
- Valor
- Disponible a la Venta
- Disponible a el Prestamo
  
##  Libros
- Id Libro
- Genero(s)
- Editorial
- Version
- Autor
- Paginas
- Titulo
- Portada
- Sinopsis

##  Usuario
- Nombre
- Email
- Contraseña
- Foto de Perfil
- Libros Comprados
- Habilitado para Prestamo?

##  Prestamo
-  Id Libro
-  Id Prestamo
-  Id Usuario
-  Tiempo Maximo de Prestamo
-  Se regreso?

##  Compras
- Tarjeta / Método de Pago
- Id Usuario
- Id Carrito
- Costo Total 
- ID Transaccion
  
##  Transaccion
- Datos de Transacciones (Los Permitidos)

##  Carrito
- ID objeto Carrito
- ID Carrito
- ID Usuario
- Id Compra

* Objeto Carrito
- Id Libro
- Cantidad
- ID Carro
