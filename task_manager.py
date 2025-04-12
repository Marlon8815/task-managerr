tareas = {}

def crear_tarea():
    titulo = input("📌 Escribe el título de la tarea: ")
    tareas[titulo] = False
    print("✅ Tarea creada correctamente.")

def listar_tareas():
    if not tareas:
        print("📭 No hay tareas registradas.")
    else:
        print("\n📋 Lista de tareas:")
        for i, (titulo, completada) in enumerate(tareas.items(), start=1):
            estado = "✅" if completada else "❌"
            print(f"{i}. {titulo} [{estado}]")

def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")

# Ejecutar menú al iniciar
mostrar_menu()
