# Diccionario donde se guardan las tareas
tareas = {}

def crear_tarea():
    titulo = input("📝 Ingrese el título de la tarea: ")
    if titulo in tareas:
        print("⚠️ La tarea ya existe.")
        return
    tareas[titulo] = False
    print(f"✅ Tarea '{titulo}' creada con éxito.")

def listar_tareas():
    if not tareas:
        print("📭 No hay tareas.")
        return

    print("\n📋 Lista de tareas:")
    for i, (titulo, completada) in enumerate(tareas.items(), 1):
        estado = "✅" if completada else "❌"
        print(f"{i}. {titulo} - {estado}")

def completar_tarea():
    if not tareas:
        print("📭 No hay tareas para completar.")
        return

    listar_tareas()

    try:
        num = int(input("✅ Ingrese el número de la tarea completada: "))
        if num < 1 or num > len(tareas):
            print("❌ Número inválido.")
            return

        titulo = list(tareas.keys())[num - 1]
        tareas[titulo] = True
        print(f"✅ Tarea '{titulo}' marcada como completada.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")

def eliminar_tarea():
    if not tareas:
        print("📭 No hay tareas para eliminar.")
        return

    listar_tareas()

    try:
        num = int(input("🗑️ Ingrese el número de la tarea que quiere eliminar: "))
        if num < 1 or num > len(tareas):
            print("❌ Número inválido.")
            return

        titulo = list(tareas.keys())[num - 1]
        del tareas[titulo]
        print(f"🗑️ Tarea '{titulo}' eliminada correctamente.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")

def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")

# Iniciar el programa
if __name__ == "__main__":
    mostrar_menu()
