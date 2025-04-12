tareas = {}

def crear_tarea():
    titulo = input("Ingresa el título de la tarea: ")
    if titulo in tareas:
        print("⚠️ Esa tarea ya existe.")
    else:
        tareas[titulo] = False
        print(f"✅ Tarea '{titulo}' creada con éxito.")

def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear tarea")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_tarea()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    mostrar_menu()
