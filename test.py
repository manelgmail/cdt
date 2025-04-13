import requests

# Cargar la tabla completa desde GitHub
def cargar_tabla():
    namespace = {}
    url = "https://raw.githubusercontent.com/manelgmail/cdt/refs/heads/main/tablaCompleta.py"
    exec(requests.get(url).text, namespace)
    return namespace["tabla"]

# Buscar la sección mínima adecuada
def obtener_seccion(tabla, metodo, tipo_cable, intensidad):
    clave = (metodo.upper(), tipo_cable.upper())
    if clave not in tabla:
        return None, f"No hay datos para el método '{metodo}' y tipo '{tipo_cable}'"
    for seccion, capacidad in tabla[clave].items():
        if capacidad >= intensidad:
            return seccion, None
    return None, "Ninguna sección soporta esa intensidad"

# Función principal de cálculo de caída de tensión
def calcular_caida_tension():
    print("🧮 CÁLCULO DE CAÍDA DE TENSIÓN EN CABLES")
    
    L = float(input("Ingrese la longitud del cable (m): "))   
    W = float(input("Ingrese Wattios (W): "))
    COS = float(input("Ingrese valor COS: "))
    
    # Calcular intensidad
    I = W / (230 * COS)
    print(f"Intensidad calculada: {I:.2f} A")

    print("\nTipo de material:")
    print("1 - Cobre")
    print("2 - Aluminio")
    M = int(input("Seleccione el material (1 o 2): "))

    if M == 1:
        rho = 0.0178  # ohm·mm²/m
    elif M == 2:
        rho = 0.0282
    else:
        print("Opción inválida. Asignando cobre por defecto.")
        rho = 0.0178

    metodo = input("Método de instalación (ej. B1, C, D...): ").strip()
    tipo = input("Tipo de cable (ej. 2xPVC, 3xXLPE): ").strip()

    tabla = cargar_tabla()
    S_normalizada, error = obtener_seccion(tabla, metodo, tipo, I)

    if error:
        print("❌", error)
        return

    # Calcular caída de tensión usando sección normalizada
    Vd = (2 * rho * L * I * COS) / S_normalizada

    # Mostrar resultados
    print(f"\n🔌 Caída de tensión: {Vd:.2f} V")
    print(f" Sección normalizada según tabla: {S_normalizada} mm²")
    
    porcentaje = (Vd / 230) * 100
    print(f"📉 Porcentaje respecto a 230V: {porcentaje:.2f}%")

# Ejecutar el programa
calcular_caida_tension()
