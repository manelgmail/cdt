def obtener_tabla():
    return {
        # Método B1
        ("B1", "2xPVC"): {
            1.5: 15.5, 2.5: 21, 4: 28, 6: 36, 10: 46, 16: 63, 25: 83, 35: 103, 50: 123,
            70: 157, 95: 191, 120: 220, 150: 252, 185: 289, 240: 344
        },
        ("B1", "3xPVC"): {
            1.5: 14.5, 2.5: 20, 4: 26, 6: 34, 10: 44, 16: 60, 25: 78, 35: 95, 50: 116,
            70: 147, 95: 178, 120: 204, 150: 233, 185: 267, 240: 317
        },
        ("B1", "2xXLPE"): {
            1.5: 18.5, 2.5: 25, 4: 33, 6: 43, 10: 59, 16: 80, 25: 104, 35: 125, 50: 148,
            70: 185, 95: 224, 120: 257, 150: 294, 185: 335, 240: 398
        },
        ("B1", "3xXLPE"): {
            1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 77, 25: 100, 35: 119, 50: 142,
            70: 177, 95: 212, 120: 243, 150: 278, 185: 317, 240: 376
        },
        # Aquí puedes añadir más métodos y tipos de cable como:
        # ("C", "2xPVC"): { ... },
        # ("D", "3xXLPE"): { ... },
    }

def calcular_seccion(metodo, tipo_cable, intensidad_requerida):
    tabla = obtener_tabla()
    clave = (metodo, tipo_cable)
    if clave not in tabla:
        return f"❌ No hay datos para el método '{metodo}' y tipo de cable '{tipo_cable}'"
    
    opciones = tabla[clave]
    for seccion, intensidad in sorted(opciones.items()):
        if intensidad >= intensidad_requerida:
            return f"✅ Sección mínima necesaria: {seccion} mm² (Soporta {intensidad} A)"
    
    return "❌ Ninguna sección disponible soporta esa intensidad"

def menu():
    print("📐 Cálculo de sección mínima de conductor (tabla ampliada)")
    metodo = input("Método de instalación (ej. B1, C, D...): ").strip()
    tipo = input("Tipo de cable (ej. 2xPVC, 3xXLPE): ").replace(" ", "")
    try:
        intensidad = float(input("Intensidad requerida (A): "))
    except ValueError:
        print("⚠️ La intensidad debe ser un número.")
        return
    resultado = calcular_seccion(metodo, tipo, intensidad)
    print("\\n" + resultado)

if __name__ == "__main__":
    menu()
