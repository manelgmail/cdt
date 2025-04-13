
# Tabla completa de intensidades máximas admisibles (fragmento)
tabla = {
    ("B1", "2xPVC"): {1.5: 14.5, 2.5: 20, 4: 26, 6: 34, 10: 46, 16: 63, 25: 82, 35: 101, 50: 122, 70: 155, 95: 187, 120: 216, 150: 247, 185: 281, 240: 330},
    ("B1", "3xXLPE"): {1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 77, 25: 100, 35: 124, 50: 151, 70: 193, 95: 234, 120: 272, 150: 313, 185: 356, 240: 419}
    # Incluir el resto de la tabla si se desea
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
