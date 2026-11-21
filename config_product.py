"""
config_product.py
Definición de las variantes de la línea de productos BiblioSPL.

Cada variante es un diccionario de características (features). El núcleo
común (catálogo, autenticación y administración) está presente en todas;
aquí solo se declaran las características variables.
"""

PRODUCT_A = {
    'NOMBRE': 'BiblioSPL Básico',
    'ENABLE_REPORTS': False,          # Exportar catálogo a PDF / CSV
    'ENABLE_NOTIFICATIONS': False,    # Avisos internos a los usuarios
    'ENABLE_ADVANCED_SEARCH': False,  # Búsqueda por autor, categoría y años
}

PRODUCT_B = {
    'NOMBRE': 'BiblioSPL Completo',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
}

PRODUCTS = {
    'A': PRODUCT_A,
    'B': PRODUCT_B,
}


def get_product(code):
    """Devuelve la configuración de la variante solicitada (A o B)."""
    code = (code or 'B').upper()
    if code not in PRODUCTS:
        raise ValueError(f"Variante desconocida: {code}. Use una de {list(PRODUCTS)}")
    return PRODUCTS[code]
