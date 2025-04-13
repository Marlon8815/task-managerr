import uuid

# Lista donde se guardan las tareas
tareas = []

def generar_id_unico():
    return str(uuid.uuid4())

def crear_tarea():
    descripcion = input("📝 Ingrese la descripción de la tarea: ")
    nueva_tarea = {
        "id": generar_id_unico(),
        "description": descripcion,
        "completed": False
    }
    tareas.append(nueva_tarea)
    print(f"✅ Tarea '{descripcion}' creada con éxito.")

def listar_tareas():
    if not tareas:
        print("📭 No hay tareas.")
        return

    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✅" if tarea["completed"] else "❌"
        print(f"{i}. {tarea['description']} - {estado} (ID: {tarea['id']})")

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
        tareas[num - 1]["completed"] = True
        print(f"✅ Tarea '{tareas[num - 1]['description']}' marcada como completada.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")

def eliminar_tarea():
    if not tareas:
        print("📭 No hay tareas para eliminar.")
        return

    listar_tareas()
    try:
        num = int(input("🗑️ Ingrese el número de la tarea a eliminar: "))
        if num < 1 or num > len(tareas):
            print("❌ Número inválido.")
            return
        tarea_eliminada = tareas.pop(num - 1)
        print(f"🗑️ Tarea '{tarea_eliminada['description']}' eliminada correctamente.")
    except ValueError:
        print("❌ Debe ingresar un número válido.")

def mostrar_menu():
    print("=== Bienvenido a Task Manager ===")
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

if __name__ == "__main__":
    mostrar_menu()
