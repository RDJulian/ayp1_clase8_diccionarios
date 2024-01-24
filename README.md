# Clase 8: Diccionarios

En esta clase vamos a ver diccionarios: qué son, como se usan y los metodos que Python provee.

# Presentación:

[Enlace a la presentación](https://docs.google.com/presentation/d/1V9ZiCz2pGA130qmPhLZQypjRYZWHrRzHhK4WxCWr0bU/edit?usp=sharing)

# Ejercicios:

### Ejercicio 1:

Escribir un programa que permita:

1. Dar de alta a un alumno, ingresando su nombre, apellido y padrón. Estos datos deben ser guardados en un diccionario.
2. Permitir la busqueda de un alumno por su nombre. Imprimir su información si se encuentra, o un mensaje de error si
   no.
3. Imprimir la información de todos los alumnos guardados. Pueden ser guardados en una lista.<br><br>

### Ejercicio 2:

La marca de prendas deportivas Algodidas, tras la victoria albiceleste en el mundial de la FIFA, tiene una demanda
altísima por las camisetas de los jugadores. Ante tal volumen de compras, decidieron pedirle ayuda a informáticos para
desarrollar un sistema que funcione como base de datos. Deberá contar con opciones de alta, baja, consulta y
modificación, cumpliendo las siguientes consignas:
<ol>
    <li>Dar de alta un nuevo <em>modelo</em> de camiseta, junto con el stock disponible para cada uno
    de los talles:
    <ol>
        <li>
            XS
        </li>
        <li>
            S
        </li>
        <li>
            M
        </li>
        <li>
            L
        </li>
        <li>
            XL
        </li>
    </ol>
    El precio ingresado <strong>será el mismo</strong> para todos los talles.
    Todos los modelos deberán ser guardados en un <em>diccionario</em>, con el nombre del modelo como llave.
    El stock inicial para cada talle será el mismo, pero deben ser contados por separado.<br>
    Ejemplos de nombres: Titular 2 estrellas, Suplente 3 estrellas, etc.
    <li>Mostrar la información de un modelo (nombre, precio y stock por talle).</li>
    <li>Dar de baja un modelo especifico, borrando totalmente los registros.</li>
    <li>Comprar una camiseta: se deberá ingresar el modelo, el talle y la cantidad de camisetas a comprar.
    </li>
    <li>Agregar stock: se deberá ingresar el modelo y la cantidad de camisetas a agregar. Se agrega para todos los talles.
    </li>
    <li>Cambiar precio: se deberá ingresar el modelo y el nuevo precio.
    <li>Salir del programa.
    </li>
</ol>

# Documentación:

[Introducción a Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)<br>
[Documentación oficial de dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
