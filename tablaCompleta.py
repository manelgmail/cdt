# Tabla completa de intensidades máximas admisibles
tabla = {
    # A1
    ("A1", "3xPVC"): {1.5: 11.5, 2.5: 15.5, 4: 20, 6: 26, 10: 36, 16: 48, 25: 63},
    ("A1", "2xPVC"): {1.5: 12.5, 2.5: 17, 4: 22, 6: 29, 10: 40, 16: 53, 25: 69},

    # A2
    ("A2", "3xPVC"): {1.5: 12.5, 2.5: 17, 4: 22, 6: 29, 10: 40, 16: 54, 25: 72, 35: 88, 50: 106, 70: 136, 95: 167, 120: 192, 150: 220, 185: 253, 240: 302},
    ("A2", "2xPVC"): {1.5: 13, 2.5: 17.5, 4: 23, 6: 30, 10: 42, 16: 56, 25: 74, 35: 92, 50: 111, 70: 143, 95: 175, 120: 201, 150: 230, 185: 265, 240: 316},

    # B1
    ("B1", "3xPVC"): {1.5: 14.5, 2.5: 20, 4: 26, 6: 34, 10: 44, 16: 60, 25: 78, 35: 95, 50: 116, 70: 147, 95: 178, 120: 204, 150: 233, 185: 267, 240: 317},
    ("B1", "2xPVC"): {1.5: 15.5, 2.5: 21, 4: 28, 6: 36, 10: 46, 16: 63, 25: 83, 35: 103, 50: 123, 70: 157, 95: 191, 120: 220, 150: 252, 185: 289, 240: 344},
    ("B1", "3xXLPE"): {1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 77, 25: 100, 35: 119, 50: 142, 70: 177, 95: 212, 120: 243, 150: 278, 185: 317, 240: 376},
    ("B1", "2xXLPE"): {1.5: 18.5, 2.5: 25, 4: 33, 6: 43, 10: 59, 16: 80, 25: 104, 35: 125, 50: 148, 70: 185, 95: 224, 120: 257, 150: 294, 185: 335, 240: 398},

    # B2
    ("B2", "3xPVC"): {1.5: 16.5, 2.5: 22, 4: 29, 6: 37, 10: 51, 16: 70, 25: 91, 35: 112, 50: 137, 70: 174, 95: 210, 120: 241, 150: 275, 185: 315, 240: 374},
    ("B2", "2xPVC"): {1.5: 17.5, 2.5: 23, 4: 31, 6: 39, 10: 53, 16: 73, 25: 94, 35: 117, 50: 142, 70: 181, 95: 219, 120: 252, 150: 287, 185: 329, 240: 391},

    # C
    ("C", "3xPVC"): {1.5: 19, 2.5: 26, 4: 34, 6: 44, 10: 60, 16: 81, 25: 106, 35: 127, 50: 151, 70: 188, 95: 224, 120: 256, 150: 291, 185: 332, 240: 392},

    # E
    ("E", "3xXLPE"): {1.5: 21, 2.5: 29, 4: 38, 6: 49, 10: 67, 16: 91, 25: 118, 35: 142, 50: 168, 70: 209, 95: 250, 120: 287, 150: 328, 185: 376, 240: 444},
    ("E", "2xXLPE"): {1.5: 21, 2.5: 30, 4: 39, 6: 50, 10: 69, 16: 94, 25: 122, 35: 147, 50: 175, 70: 218, 95: 261, 120: 299, 150: 341, 185: 392, 240: 463},

    # F
    ("F", "3xXLPE"): {1.5: 21, 2.5: 30, 4: 40, 6: 51, 10: 70, 16: 94, 25: 121, 35: 145, 50: 173, 70: 216, 95: 260, 120: 297, 150: 338, 185: 387, 240: 457},
    ("F", "2xXLPE"): {1.5: 23, 2.5: 31, 4: 41, 6: 52, 10: 72, 16: 97, 25: 125, 35: 150, 50: 179, 70: 222, 95: 267, 120: 305, 150: 349, 185: 400, 240: 472},
}

def calcular_seccion(metodo, tipo_cable, intensidad_requerida):
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
    print("\n" + resultado)

if __name__ == "__main__":
    menu()
