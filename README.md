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

### acciones de Inventario
- Listar por (Autor, Genero, Fecha de Publicacion)
- CRUD Inventario (Excepto Crear, los libros se crean desde su propia clase)
- TBT 
  
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

### acciones de Libros
- Crud Libros


## Generos
- Nombre
- ID

### acciones de Generos
- CRUD Generos

## Genero de Libro (Clase generada para unir varios Generos a un mismo Libro) 
ID Libro
ID Genero

##  Usuario
- Nombre
- Email
- Telefono
- Contraseña
- Foto de Perfil
- Libros Comprados
- Habilitado para Prestamo?

### acciones de usuarios
- CRUD Usuario
- Cambiar Foto Perfil
- Solicitar Prestamos
- Hacer Compras
- Devolver Libro
- Generar Usuarios (nivel cliente y nivel empresarial**)
- Desactivar Usuarios

##  Prestamo
-  Id Libro
-  Id Prestamo
-  Id Usuario
-  Fecha Inicial
-  Fecha Regresado
-  Fecha Limite
-  Se regreso?
-  Comentarios Extras
-  Estado en el prestamo
-  Estado en la Devolucion

##  Compras
- Tarjeta / Método de Pago
- Id Usuario
- Id Carrito
- Costo Total 
- ID Transaccion
  

## Metodo Pago
- Fecha de La Transaccion (Para ambos tipos)
- Tipo (Tarjeta / Efectivo)
- (si es Tarjeta) Debito / Credito
- Nro Tarjeta
- Cuotas

- (Si es Efectivo) no se agrega nada 


##  Carrito
- ID objeto Carrito
- ID Carrito
- ID Usuario
- Id Compra

## Objeto Carrito
- Id Libro
- Cantidad
- ID Carro
