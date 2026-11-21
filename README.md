# BiblioSPL – Línea de productos de software basada en Django

Práctica 4 · Gestión de la Configuración de Software (UNEMI)
Integrantes: Marlon Rainier Aguiño Salinas · Erick Steven Terranova Vega

## Instalación
```bash
pip install django reportlab
python manage.py migrate
python manage.py cargar_demo          # libros de ejemplo + usuario demo / demo12345
```

## Ejecutar una variante
| Variante | Producto | Comando (Linux/macOS) | Windows PowerShell |
|---|---|---|---|
| A | BiblioSPL Básico | `PRODUCT_VARIANT=A python manage.py runserver` | `$env:PRODUCT_VARIANT="A"; python manage.py runserver` |
| B | BiblioSPL Completo | `PRODUCT_VARIANT=B python manage.py runserver` | `$env:PRODUCT_VARIANT="B"; python manage.py runserver` |

Si no se define `PRODUCT_VARIANT`, se ejecuta la Variante B.

## Activar / desactivar características
Edite `config_product.py` y cambie las banderas `ENABLE_REPORTS`, `ENABLE_NOTIFICATIONS`
y `ENABLE_ADVANCED_SEARCH` de la variante deseada. Reinicie el servidor.

## Estructura
- `core/`, `cuentas/` → núcleo común
- `reportes/`, `notificaciones/`, `busqueda/` → apps opcionales
- `config_product.py` → definición de variantes
