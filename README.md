# Sistema de Gestión Académica de Estudiantes

Este es un sistema de gestión académica desarrollado en Python para registrar, consultar, actualizar y eliminar estudiantes, junto con sus respectivas notas.

## Características

- Registrar estudiantes con ID único, nombre, edad y 3 notas.
- Consultar información detallada de un estudiante.
- Actualizar las notas de un estudiante existente.
- Eliminar estudiantes por ID.
- Ver todos los estudiantes registrados con promedio de notas.
- Menú interactivo en consola.

## Estructura de Datos

Los estudiantes se almacenan en una lista de diccionarios con la siguiente estructura:

"
  "id": "123",
  
  "nombre": "Juan Pérez",
  
  "edad": 20,
  
  "notas": [4.5, 3.7, 5.0]
"

##Requisitos

Python 3.6 o superior

Consola o terminal para ejecutar scripts interactivos

-Cómo usar

Clona este repositorio o descarga el archivo gestion_estudiantes.py.

Abre una terminal y ejecuta el archivo:

-Usa el menú para interactuar con el sistema.

1. Registrar estudiante
2. Consultar estudiante
3. Actualizar notas
4. Eliminar estudiante
5. Ver todos los estudiantes
6. Salir

##Validaciones implementadas

ID: único y numérico.

Nombre: solo letras y espacios.

Edad: número entero positivo (hasta 80).

Notas: tres valores numéricos entre 0.0 y 5.0.


-Desarrollado por Ehider Estiven Villanueva Perez.
