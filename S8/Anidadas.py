# =========================
# Gestión de gastos personales
# =========================

# Estructura principal: lista de diccionarios
gastos = []


def añadir_gasto(fecha, categoria, cantidad):
    """Añade un nuevo gasto controlando errores y duplicados."""
    # Validaciones
    if not fecha or not categoria or cantidad is None:
        raise ValueError("Ningún campo puede estar vacío.")
    if not isinstance(fecha, str) or not isinstance(categoria, str):
        raise TypeError("La fecha y la categoría deben ser cadenas de texto.")
    if not isinstance(cantidad, (int, float)):
        raise TypeError("La cantidad debe ser numérica.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    
    # Evitar duplicados (fecha + categoría + cantidad)
    for gasto in gastos:
        if gasto["fecha"] == fecha and gasto["categoria"] == categoria and gasto["cantidad"] == cantidad:
            raise ValueError("El registro ya existe.")
    
    # Añadir gasto
    gastos.append({"fecha": fecha, "categoria": categoria, "cantidad": cantidad})
    print("✅ Gasto añadido correctamente.")


def buscar_por_categoria(categoria):
    """Devuelve todos los gastos que pertenezcan a una categoría dada."""
    if not categoria:
        raise ValueError("La categoría no puede estar vacía.")
    resultado = [g for g in gastos if g["categoria"].lower() == categoria.lower()]
    return resultado


def gasto_promedio():
    """Calcula el gasto promedio."""
    if not gastos:
        raise ValueError("No hay registros para calcular la media.")
    total = sum(g["cantidad"] for g in gastos)
    return total / len(gastos)


def gasto_maximo():
    """Devuelve el gasto más alto registrado."""
    if not gastos:
        raise ValueError("No hay registros para calcular el máximo.")
    return max(gastos, key=lambda g: g["cantidad"])


# =========================
# Ejemplo de uso
# =========================
if __name__ == "__main__":
    try:
        añadir_gasto("2025-11-01", "Comida", 25.5)
        añadir_gasto("2025-11-02", "Transporte", 10)
        añadir_gasto("2025-11-03", "Comida", 15)
        
        print("\n🔍 Buscar categoría 'Comida':")
        print(buscar_por_categoria("Comida"))
        
        print("\n📊 Gasto promedio:", gasto_promedio())
        print("💰 Gasto máximo:", gasto_maximo())
    
    except Exception as e:
        print("⚠️ Error:", e)
