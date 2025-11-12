def pedir_numero(mensaje):
    """Pide un número entero al usuario con control de errores."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Debes ingresar un número entero.")


def obtener_notas(cantidad):
    """Solicita las notas de los alumnos y las devuelve en una lista."""
    notas = []
    for i in range(cantidad):
        nota = pedir_numero(f"Introduce la nota del alumno {i + 1}: ")
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("⚠️ La nota debe estar entre 0 y 10. Intenta de nuevo.")
            i -= 1  # reintentar la nota actual
    return notas


def calcular_media(notas):
    """Calcula y devuelve la media de una lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)


def mostrar_aprobados(notas):
    """Muestra las notas aprobadas."""
    aprobados = [nota for nota in notas if nota >= 5]
    if aprobados:
        print("✅ Aprobados:")
        for nota in aprobados:
            print(nota)
    else:
        print("❌ No hay aprobados.")


def programa():
    """Función principal del programa."""
    print("=== Programa de Notas ===")
    cantidad = pedir_numero("¿Cuántos alumnos hay? ")

    if cantidad <= 0:
        print("No hay alumnos para procesar.")
        return

    notas = obtener_notas(cantidad)
    media = calcular_media(notas)

    print(f"\n📊 Media del grupo: {media:.2f}")
    mostrar_aprobados(notas)


# Ejecutar el programa
if __name__ == "__main__":
    programa()
