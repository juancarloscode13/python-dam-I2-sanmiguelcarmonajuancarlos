# usar_analisis.py

import aux_precios  # Importamos el archivo con las funciones

# Lista de precios de ejemplo
precios = [25.5, 18.0, 30.2, 22.9, 27.5, 19.9]

print("Lista de precios:", precios)
print("Precio máximo:", aux_precios.precio_maximo(precios))
print("Precio mínimo:", aux_precios.precio_minimo(precios))
print("Precio promedio:", round(aux_precios.precio_promedio(precios), 2))
print("Diferencia entre máximo y mínimo:", aux_precios.diferencia_max_min(precios))

print("\nPrecios ordenados de menor a mayor:", aux_precios.ordenar_precios(precios))
print("Precios ordenados de mayor a menor:", aux_precios.ordenar_precios(precios, descendente=True))
