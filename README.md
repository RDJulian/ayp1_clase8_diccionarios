# Clase 8: Diccionarios

En esta clase vamos a ver diccionarios: qué son, como se usan y los metodos que Python provee.

# Presentación:

[Enlace a la presentación](https://docs.google.com/presentation/d/1sOnLCIYSglnRJEieR-R55GDUoq-nIQq1QR2lYf--cTA/edit?usp=sharing\])

# Ejercicio:

La marca de prendas deportivas Algodidas, tras la victoria albiceleste en el mundial de la FIFA, tiene una demanda
altísima por las camisetas de los jugadores. Ante tal volumen de compras, decidieron pedirle ayuda a informáticos para
desarrollar un sistema que funcione como base de datos. Deberá contar con opciones de alta, baja, consulta y
modificación, cumpliendo las siguientes consignas:
<ol>
    <li>Dar de alta un nuevo <em>modelo</em> de camiseta y deberá contar con el stock disponible para cada uno
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
    ej: Titular 2 estrellas, Suplente 3 estrellas, etc.
    <li>Dar de baja un modelo especifico, borrando totalmente los registros.</li>
    <li>Comprar una camiseta: se deberá ingresar el modelo, el talle y la cantidad de camisetas a comprar.
    </li>
    <li>Agregar stock: se deberá ingresar el modelo y la cantidad de camisetas a agregar. Se agrega para todos los talles.
    </li>
    <li>Cambiar precio: se deberá ingresar el modelo y el nuevo precio.
    </li>
    <li>Calcular, dado un modelo, el valor total en base al precio y a la cantidad de camisetas.
    <li>Mostrar el valor final de las ventas. Se debe considerar el precio de una camiseta al momento de la compra.
    </li>
    <li>Salir del programa.
    </li>
</ol>
<strong>IMPORTANTE</strong>: Considerar para todas las opciones los casos bordes o no válidos.

# Tarea:

Refactorizar y ampliar el codigo del Ejercicio 2, utilizando los metodos vistos y los conocimientos adquiridos hasta
ahora. Pensar si es conveniente iterar, validar los valores ingresados, mejorar la interaccion con el usuario, escribir
pre y postcondiciones, etc.

# Documentación:

[Introducción a Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)<br>
[Documentación oficial de dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
