# Diccionario con 10 socios de ejemplo
socios = {
    "Juan Pérez": 30.0,
    "Ana López": 25.5,
    "Carlos Gómez": 40.0,
    "Lucía Fernández": 35.0,
    "Miguel Torres": 28.0,
    "Elena Ruiz": 33.5,
    "Pedro Ramírez": 29.9,
    "Laura Martínez": 32.0,
    "Diego Sánchez": 26.5,
    "Sofía Navarro": 31.0
}

# Bucle principal del programa
while True:
    print("\n--- GESTIÓN DE SOCIOS DEL GIMNASIO ---")
    print("1. Insertar socio")
    print("2. Eliminar socio")
    print("3. Modificar cuota de un socio")
    print("4. Mostrar todos los socios y cuotas")
    print("5. Calcular media de ingresos por socio")
    print("6. Salir")
    
    opcion = input("Elige una opción (1-6): ")

    match opcion:
        case "1":
            nombre = input("Introduce el nombre del socio: ")
            if nombre in socios:
                print("Ese socio ya existe.")
            else:
                try:
                    cuota = float(input("Introduce la cuota mensual (€): "))
                    socios[nombre] = cuota
                    print(f"Socio '{nombre}' añadido con cuota de {cuota}€.")
                except ValueError:
                    print("Por favor, introduce un número válido para la cuota.")

        case "2":
            nombre = input("Introduce el nombre del socio a eliminar: ")
            if nombre in socios:
                del socios[nombre]
                print(f"Socio '{nombre}' eliminado.")
            else:
                print("Ese socio no existe.")

        case "3":
            nombre = input("Introduce el nombre del socio a modificar: ")
            if nombre in socios:
                try:
                    nueva_cuota = float(input("Introduce la nueva cuota (€): "))
                    socios[nombre] = nueva_cuota
                    print(f"Cuota de '{nombre}' actualizada a {nueva_cuota}€.")
                except ValueError:
                    print("Por favor, introduce un número válido para la cuota.")
            else:
                print("Ese socio no existe.")

        case "4":
            if socios:
                print("\n--- LISTA DE SOCIOS Y CUOTAS ---")
                for nombre, cuota in socios.items():
                    print(f"Socio: {nombre} | Cuota: {cuota}€")
            else:
                print("No hay socios registrados.")

        case "5":
            if socios:
                media = sum(socios.values()) / len(socios)
                print(f"La media de ingresos por socio es: {media:.2f}€")
            else:
                print("No hay socios para calcular la media.")

        case "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        case _:
            print("Opción no válida. Elige un número del 1 al 6.")
