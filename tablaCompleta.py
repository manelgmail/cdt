# Tabla completa de intensidades máximas admisibles
tabla = {
    # A1
    ("A1", "3xPVC"): {1.5: 11.5, 2.5: 15.5, 4: 20, 6: 26, 10: 36, 16: 48, 25: 63},
    ("A1", "2xPVC"): {1.5: 12.5, 2.5: 17, 4: 22, 6: 29, 10: 40, 16: 53, 25: 69},
    ("A1", "3xXLPE"): {1.5: 15.5, 2.5: 20, 4: 28, 6: 36, 10: 49, 16: 66, 25: 86, 35: 106, 50: 128, 70: 162, 95: 196, 120: 226, 150: 259, 185: 294, 240: 345},
    ("A1", "2xXLPE"): {1.5: 16.5, 2.5: 22, 4: 30, 6: 39, 10: 54, 16: 72, 25: 91, 35: 114, 50: 139, 70: 178, 95: 216, 120: 251, 150: 289, 185: 329, 240: 385},

    # A2
    ("A2", "3xPVC"): {1.5: 11, 2.5: 15, 4: 20, 6: 25, 10: 33, 16: 45, 25: 59},
    ("A2", "2xPVC"): {1.5: 11.5, 2.5: 15.5, 4: 20, 6: 26, 10: 36, 16: 48, 25: 63},
    ("A2", "3xXLPE"): {1.5: 14, 2.5: 19, 4: 25, 6: 32, 10: 45, 16: 61, 25: 80, 35: 100, 50: 121, 70: 155, 95: 188, 120: 217},
    ("A2", "2xXLPE"): {1.5: 15.5, 2.5: 20, 4: 28, 6: 36, 10: 49, 16: 66, 25: 86, 35: 106, 50: 128, 70: 162, 95: 196, 120: 226, 150: 259, 185: 294, 240: 345},

    # B1
    ("B1", "3xPVC"): {1.5: 13.5, 2.5: 18, 4: 24, 6: 31, 10: 43, 16: 59, 25: 77, 35: 95, 50: 116, 70: 148, 95: 180, 120: 207},
    ("B1", "2xPVC"): {1.5: 14.5, 2.5: 20, 4: 26, 6: 34, 10: 46, 16: 63, 25: 82, 35: 101, 50: 122, 70: 155, 95: 187, 120: 216, 150: 247, 185: 281, 240: 330},
    ("B1", "3xXLPE"): {1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 77, 25: 100, 35: 124, 50: 151, 70: 193, 95: 234, 120: 272, 150: 313, 185: 356, 240: 419},
    ("B1", "2xXLPE"): {1.5: 20, 2.5: 28, 4: 38, 6: 49, 10: 68, 16: 91, 25: 115, 35: 143, 50: 174, 70: 223, 95: 271, 120: 314, 150: 359, 185: 409, 240: 489},

    # B2
    ("B2", "3xPVC"): {1.5: 12.5, 2.5: 17, 4: 22, 6: 29, 10: 40, 16: 53, 25: 69},
    ("B2", "2xPVC"): {1.5: 13.5, 2.5: 18, 4: 24, 6: 31, 10: 43, 16: 59, 25: 77, 35: 95, 50: 116, 70: 148, 95: 180, 120: 207},
    ("B2", "3xXLPE"): {1.5: 16.5, 2.5: 22, 4: 30, 6: 39, 10: 54, 16: 72, 25: 91, 35: 114, 50: 139, 70: 178, 95: 216, 120: 251, 150: 289, 185: 329, 240: 385},
    ("B2", "2xXLPE"): {1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 77, 25: 100, 35: 124, 50: 151, 70: 193, 95: 234, 120: 272, 150: 313, 185: 356, 240: 419},

    # C
    ("C", "3xPVC"): {1.5: 14.5, 2.5: 20, 4: 26, 6: 34, 10: 46, 16: 63, 25: 82, 35: 101, 50: 122, 70: 155, 95: 187, 120: 216, 150: 247, 185: 281, 240: 330},
    ("C", "2xPVC"): {1.5: 17, 2.5: 23, 4: 31, 6: 40, 10: 54, 16: 73, 25: 95, 35: 119, 50: 145, 70: 185, 95: 224, 120: 260, 150: 299, 185: 341, 240: 401},
    ("C", "3xXLPE"): {1.5: 20, 2.5: 27, 4: 36, 6: 46, 10: 63, 16: 85, 25: 108, 35: 133, 50: 162, 70: 208, 95: 252, 120: 293, 150: 337, 185: 385, 240: 455},
    ("C", "2xXLPE"): {1.5: 21, 2.5: 30, 4: 40, 6: 52, 10: 72, 16: 97, 25: 122, 35: 153, 50: 188, 70: 243, 95: 298, 120: 350, 150: 401, 185: 460, 240: 545},

    # E
    ("E", "3xPVC"): {1.5: 16, 2.5: 21, 4: 29, 6: 37, 10: 52, 16: 69, 25: 87, 35: 109, 50: 133, 70: 170, 95: 207, 120: 240, 150: 276, 185: 314, 240: 368},
    ("E", "2xPVC"): {1.5: 19, 2.5: 26, 4: 34, 6: 44, 10: 60, 16: 81, 25: 103, 35: 127, 50: 155, 70: 199, 95: 241, 120: 280, 150: 322, 185: 368, 240: 435},
    ("E", "3xXLPE"): {1.5: 20, 2.5: 28, 4: 38, 6: 49, 10: 68, 16: 91, 25: 115, 35: 143, 50: 174, 70: 223, 95: 271, 120: 314, 150: 359, 185: 409, 240: 489},
    ("E", "2xXLPE"): {1.5: 23, 2.5: 32, 4: 44, 6: 57, 10: 78, 16: 104, 25: 135, 35: 168, 50: 204, 70: 262, 95: 320, 120: 373, 150: 330, 185: 493, 240: 583},

    # F
    ("F", "3xPVC"): {1.5: 17, 2.5: 23, 4: 31, 6: 40, 10: 54, 16: 73, 25: 95, 35: 119, 50: 145, 70: 185, 95: 224, 120: 260, 150: 299, 185: 341, 240: 401},
    ("F", "2xPVC"): {1.5: 20, 2.5: 26, 4: 36, 6: 46, 10: 65, 16: 87, 25: 110, 35: 137, 50: 167, 70: 214, 95: 259, 120: 301, 150: 343, 185: 391, 240: 468},
    ("F", "3xXLPE"): {1.5: 21, 2.5: 30, 4: 40, 6: 52, 10: 72, 16: 97, 25: 122, 35: 153, 50: 188, 70: 243, 95: 298, 120: 350, 150: 401, 185: 460, 240: 545},
    ("F", "2xXLPE"): {25: 146, 35: 182, 50: 220, 70: 282, 95: 343, 120: 397, 150: 458, 185: 523, 240: 617},
}

def obtener_seccion(metodo, tipo_cable, intensidad_requerida):
    clave = (metodo.upper(), tipo_cable)
    if clave not in tabla:
        raise ValueError(f"No hay datos para el método '{metodo}' y tipo de cable '{tipo_cable}'")
    
    opciones = tabla[clave]
    for seccion, intensidad in sorted(opciones.items()):
        if intensidad >= intensidad_requerida:
            return seccion, intensidad
    
    raise ValueError("Ninguna sección disponible soporta esa intensidad")

def calcular_caida_tension():
    print("🧮 CÁLCULO DE CAÍDA DE TENSIÓN EN CABLES")

    L = float(input("Ingrese la longitud del cable (m): "))
    W = float(input("Ingrese Wattios (W): "))
    COS = float(input("Ingrese valor COS: "))
    metodo = input("Método de instalación (ej. B1): ").strip()
    tipo = input("Tipo de cable (ej. 3xXLPE): ").strip()

    I = W / (230 * COS)

    # Intensidades e IGA normalizadas
    intensidades_normalizadas = [10, 16, 20, 25, 32, 40, 50, 63]
    I_normalizada = next((i for i in intensidades_normalizadas if i >= I), None)

    print("Tipo de material:")
    print("1 - Cobre")
    print("2 - Aluminio")
    M = int(input("Seleccione el material (1 o 2): "))

    rho = 0.0178 if M == 1 else 0.0282

    try:
        seccion_norm, intensidad_norm = obtener_seccion(metodo, tipo, I)
    except ValueError as e:
        print(f"❌ Error: {e}")
        return

    S_teorica = (2 * rho * L * I * COS) / 2.3

    # Secciones normalizadas
    secciones_normalizadas = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240]
    S_normalizada = next((s for s in secciones_normalizadas if s >= S_teorica), None)

    Vd = (2 * rho * L * I * COS) / S_normalizada
    porcentaje = (Vd / 230) * 100

    print(f"\n🔌 Caída de tensión: {Vd:.2f} V")
    print(f"📏 Sección teórica calculada: {S_teorica:.2f} mm²")
    print(f"📏 Sección normalizada usada: {S_normalizada} mm²")
    print(f"📏 Sección según tabla: {seccion_norm} mm² (soporta hasta {intensidad_norm} A)")
    print(f"⚡ Intensidad calculada: {I:.2f} A")
    print(f"⚡ Intensidad normalizada usada: {I_normalizada} A")
    print(f"📉 Porcentaje respecto a 230V: {porcentaje:.2f}%")

if __name__ == "__main__":
    calcular_caida_tension()
