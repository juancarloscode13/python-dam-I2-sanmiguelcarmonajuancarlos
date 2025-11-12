import datetime

def agregar_tarea(lista_tareas, tarea):
    """Agrega una tarea a la lista con la fecha actual."""
    fecha = datetime.date.today()
    lista_tareas.append((tarea, fecha))
    return lista_tareas


def mostrar_tareas(lista_tareas):
    """Muestra todas las tareas guardadas."""
    if not lista_tareas:
        print("No hay tareas pendientes.")
        return
    print("\n📋 Tareas pendientes:")
    for i, (tarea, fecha) in enumerate(lista_tareas, start=1):
        print(f"{i}. {tarea} (Agregada el {fecha})")


def eliminar_tarea(lista_tareas, indice):
    """Elimina una tarea según su número en la lista."""
    try:
        tarea_eliminada = lista_tareas.pop(indice - 1)
        print(f"✅ Tarea eliminada: '{tarea_eliminada[0]}'")
    except IndexError:
        print("❌ Error: número de tarea no válido.")
    return lista_tareas


def menu():
    """Función principal del programa."""
    tareas = []

    while True:
        print("\n--- MENÚ DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("❌ Debes ingresar un número del 1 al 4.")
            continue

        # Sustituimos los elif por un match
        match opcion:
            case 1:
                tarea = input("Escribe la tarea: ")
                tareas = agregar_tarea(tareas, tarea)
                print("✅ Tarea agregada correctamente.")
            case 2:
                mostrar_tareas(tareas)
            case 3:
                mostrar_tareas(tareas)
                try:
                    indice = int(input("Número de tarea a eliminar: "))
                    tareas = eliminar_tarea(tareas, indice)
                except ValueError:
                    print("❌ Debes ingresar un número válido.")
            case 4:
                print("👋 ¡Hasta luego! Buen trabajo hoy.")
                break
            case _:
                print("❌ Opción no válida. Elige del 1 al 4.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()
