# Lista para almacenar los datos de los estudiantes como diccionarios individuales.
# Cada estudiante se representa como un diccionario con claves: id, nombre, edad y notas.
# Se utiliza una lista en lugar de un diccionario para evitar malas prácticas asociadas a claves duplicadas y facilitar recorridos.
estudiantes = []

# ----------------------- UTILIDADES -----------------------
def calcular_promedio(notas):
    # Calcula el promedio aritmético de una lista de notas.
    # sum(notas): suma todos los elementos.
    # len(notas): cuenta cuántos elementos hay.
    return sum(notas) / len(notas)

def validar_entero_positivo(mensaje, maximo=None):
    # Solicita un número entero positivo al usuario.
    # Utiliza .isdigit() para verificar que todos los caracteres sean dígitos.
    # .strip() elimina espacios antes y después de la entrada.
    entrada = input(mensaje).strip()
    if entrada.isdigit():  # Verifica si es un número entero positivo
        numero = int(entrada)
        if numero > 0 and (maximo is None or numero <= maximo):
            return numero
        print("[ERROR] Número fuera de rango.")
    else:
        print("[ERROR] Numero invalido.")
    return validar_entero_positivo(mensaje, maximo)

def validar_nombre(mensaje):
    # Solicita un nombre y valida que solo contenga letras y espacios.
    # .replace(" ", "") elimina espacios para validar solo las letras con isalpha().
    entrada = input(mensaje).strip()
    if entrada and entrada.replace(" ", "").isalpha():
        return entrada
    print("[ERROR] Añade solo letras y espacios.")
    return validar_nombre(mensaje)

def validar_nota(mensaje):
    # Valida que la nota ingresada sea un número  entre 0.0 y 5.0.
    entrada = input(mensaje).strip()
    try:
        nota = float(entrada)  #  convierte a número decimal
        if 0.0 <= nota <= 5.0:
            return nota
        print("[ERROR] La nota debe estar entre 0.0 y 5.0.")
    except ValueError:
        # Ocurre si la conversión a float falla (por caracteres inválidos)
        print("[ERROR] Caracteres inválidos.")
    return validar_nota(mensaje)

# -------------------- FUNCIONES PRINCIPALES --------------------
def registrar_estudiante():
    # Registra un nuevo estudiante si su ID no está repetido.
    # .append agrega un nuevo diccionario a la lista de estudiantes.
    id = str(validar_entero_positivo("Ingrese ID del estudiante: "))
    if any(est['id'] == id for est in estudiantes):
        print("[ERROR] ID ya registrado.")
        return

    nombre = validar_nombre("Ingrese nombre: ")
    edad = validar_entero_positivo("Ingrese edad (máx. 80): ", 80)
    notas = [validar_nota(f"Nota {i+1} (0.0 - 5.0): ") for i in range(3)]

    estudiantes.append({"id": id, "nombre": nombre, "edad": edad, "notas": notas})
    print("[OK] Estudiante registrado.")

def verificar_registro():
    # Verifica que haya al menos un estudiante registrado antes de continuar.
    # Utilizado para prevenir errores en otras funciones que requieren datos.
    if not estudiantes:
        print("[ADVERTENCIA] Registre al menos un estudiante antes de continuar.")
        return False
    return True

def buscar_estudiante(id):
    # Busca un estudiante en la lista por su ID.
    # Si lo encuentra, retorna el diccionario completo del estudiante.
    for est in estudiantes:
        if est['id'] == id:
            return est
    return None

def consultar_estudiante():
    # Muestra los datos de un estudiante específico por su ID.
    if not verificar_registro(): return
    id = input("ID del estudiante: ").strip()
    est = buscar_estudiante(id)
    if est:
        promedio = calcular_promedio(est["notas"])
        print(f"Nombre: {est['nombre']}\nEdad: {est['edad']}\nNotas: {est['notas']}\nPromedio: {promedio:.2f}")
    else:
        print("[ERROR] Estudiante no encontrado.")

def actualizar_notas():
    # Actualiza las notas de un estudiante si su ID existe.
    if not verificar_registro(): return
    id = input("ID del estudiante: ").strip()
    est = buscar_estudiante(id)
    if est:
        est["notas"] = [validar_nota(f"Nueva nota {i+1} (0.0 - 5.0): ") for i in range(3)]
        print("[OK] Notas actualizadas.")
    else:
        print("[ERROR] Estudiante no encontrado.")

def eliminar_estudiante():
    # Elimina un estudiante de la lista si su ID coincide.
    # .remove elimina un diccionario específico de la lista.
    if not verificar_registro(): return
    id = input("ID del estudiante: ").strip()
    est = buscar_estudiante(id)
    if est:
        estudiantes.remove(est)
        print("[OK] Estudiante eliminado.")
    else:
        print("[ERROR] Estudiante no encontrado.")

def ver_todos_los_estudiantes():
    # Muestra todos los estudiantes registrados con su información completa.
    if not verificar_registro(): return
    print("\n--- Listado de Estudiantes ---")
    for est in estudiantes:
        promedio = calcular_promedio(est["notas"])
        print(f"\nID: {est['id']}\nNombre: {est['nombre']}\nEdad: {est['edad']}\nNotas: {est['notas']}\nPromedio: {promedio:.2f}")

# -------------------------- MENÚ --------------------------
def menu():
    # Función principal que ejecuta el menú interactivo del sistema de estudiantes.
    # Usa un diccionario para asociar las opciones del menú con las funciones.
    opciones = {
        "1": registrar_estudiante,
        "2": consultar_estudiante,
        "3": actualizar_notas,
        "4": eliminar_estudiante,
        "5": ver_todos_los_estudiantes
    }

    seleccion = None
    while seleccion != "6":
        print("\n--- MENÚ ---")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Actualizar notas")
        print("4. Eliminar estudiante")
        print("5. Ver todos los estudiantes")
        print("6. Salir")

        seleccion = input("Seleccione opción (1-6): ").strip()
        accion = opciones.get(seleccion)

        if seleccion == "6":
            print("Saliendo... ¡Hasta pronto!")
        elif accion:
            accion()
        else:
            print("[ERROR] Opción inválida. Elija del 1 al 6.")

# Menu con el que el usuario podra interactuar 
    menu()
