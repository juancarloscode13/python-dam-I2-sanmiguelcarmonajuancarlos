# analisis_precios.py
#Versión sin manejo de errores.
'''
def precio_maximo(precios):
    """Devuelve el precio más alto de la lista."""
    return max(precios)

def precio_minimo(precios):
    """Devuelve el precio más bajo de la lista."""
    return min(precios)

def precio_promedio(precios):
    """Devuelve el promedio de los precios."""
    return sum(precios) / len(precios)

def diferencia_max_min(precios):
    """Devuelve la diferencia entre el precio más alto y el más bajo."""
    return precio_maximo(precios) - precio_minimo(precios)

def ordenar_precios(precios, descendente=False):
    """Devuelve la lista de precios ordenada (por defecto, de menor a mayor)."""
    return sorted(precios, reverse=descendente)
'''

# analisis_precios.py

def validar_lista_precios(precios):
    """Verifica que precios sea una lista o tupla de números."""
    if not isinstance(precios, (list, tuple)):
        raise TypeError("El parámetro debe ser una lista o tupla.")
    if not precios:
        raise ValueError("La lista de precios está vacía.")
    for p in precios:
        if not isinstance(p, (int, float)):
            raise TypeError(f"Todos los elementos deben ser números. Se encontró: {p}")
    return True


def precio_maximo(precios):
    """Devuelve el precio más alto de la lista."""
    try:
        validar_lista_precios(precios)
        return max(precios)
    except Exception as e:
        print("Error en precio_maximo:", e)


def precio_minimo(precios):
    """Devuelve el precio más bajo de la lista."""
    try:
        validar_lista_precios(precios)
        return min(precios)
    except Exception as e:
        print("Error en precio_minimo:", e)


def precio_promedio(precios):
    """Devuelve el promedio de los precios."""
    try:
        validar_lista_precios(precios)
        return sum(precios) / len(precios)
    except Exception as e:
        print("Error en precio_promedio:", e)


def diferencia_max_min(precios):
    """Devuelve la diferencia entre el precio más alto y el más bajo."""
    try:
        validar_lista_precios(precios)
        return precio_maximo(precios) - precio_minimo(precios)
    except Exception as e:
        print("Error en diferencia_max_min:", e)


def ordenar_precios(precios, descendente=False):
    """Devuelve la lista de precios ordenada (por defecto, de menor a mayor)."""
    try:
        validar_lista_precios(precios)
        return sorted(precios, reverse=descendente)
    except Exception as e:
        print("Error en ordenar_precios:", e)
