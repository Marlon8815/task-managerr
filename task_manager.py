# Diccionario para almacenar las tareas: {'tarea': False} si está pendiente, True si está completada
tareas = {}

# Crear una tarea nueva
def crear_tarea():
    titulo = input("📝 Ingresa el título de la nueva tarea: ")
    if titulo in tareas:
        print("⚠️ Esa tarea ya existe.")
    else:
        tareas[titulo] = False
        print(f"✅ Tarea '{titulo}' creada.")

# Listar todas las tareas
def listar_tareas():
    if not tareas:
        print("📭 No hay tareas registradas.")
        return
    print("\n📋 Lista de tareas:")
    for i, (titulo, completada) in enumerate(tareas.items(), start=1):
        estado = "✅" if completada else "❌"
        print(f"{i}. {titulo} [{estado}]")

# Marcar una tarea como completada
def completar_tarea():
    if not tareas:
        print("📭 No hay tareas para completar.")
        return

    listar_tareas()

    try:
        num = int(input("🔢 Ingrese el número de la tarea que quiere marcar como completada: "))
        if num < 1 or num > len(tareas):
            print("❌ Número inválido.")
            return

        titulo = list(tareas.keys())[num - 1]
        tareas[titulo] = True
        print(f"✅ Tarea '{titulo}' marcada como completada.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")

# Menú principal
def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")

# Iniciar el programa
mostrar_menu()
